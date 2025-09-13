import os
import requests
from fastapi import FastAPI, Depends , HTTPException, status , Query ,Depends
from app.auth import hash_password, verify_password, create_access_token, SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from app.advisory import get_advisory
from .db import SessionLocal, Query as QueryDB, init_db ,Scheme
from sqlalchemy.orm import Session
from app.db import Farmer
from .crops import CROPS_DATA
from .soil import SOIL_DATA
from .market_rates import MARKET_RATES
# Load env + init DB
load_dotenv()
init_db()

app = FastAPI(title="Crop-Guru API", version="0.1")

# Configure CORS
origins = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "*").split(",")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# -------------------
# Pydantic Input Model
# -------------------
class QueryIn(BaseModel):
    message: str
    crop: str | None = None
    city: str | None = "Delhi"
    locale: str | None = "en-IN"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

class FarmerIn(BaseModel):
    name: str
    phone: str
    password: str
    location: str | None = None
    crops: str | None = None

class LoginIn(BaseModel):
    phone: str
    password: str

# -------------------
# Routes
# -------------------

@app.post("/signup")
def signup(farmer: FarmerIn, db: Session = Depends(get_db)):
    if db.query(Farmer).filter(Farmer.phone == farmer.phone).first():
        raise HTTPException(status_code=400, detail="Phone already registered")

    new_farmer = Farmer(
        name=farmer.name,
        phone=farmer.phone,
        password=hash_password(farmer.password),
        location=farmer.location,
        crops=farmer.crops,
    )
    db.add(new_farmer)
    db.commit()
    db.refresh(new_farmer)

    # ✅ Improvement: Return the new farmer's name for immediate display
    return {
        "id": new_farmer.id,
        "phone": new_farmer.phone,
        "name": new_farmer.name,
        "message": "Signup successful"
    }

@app.post("/login")
def login(login: LoginIn, db: Session = Depends(get_db)):
    farmer = db.query(Farmer).filter(Farmer.phone == login.phone).first()
    if not farmer or not verify_password(login.password, farmer.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(farmer.id)})

    # ✅ Improvement: Return the farmer's name with the access token
    return {
        "access_token": token,
        "farmer_id": farmer.id,
        "farmer_name": farmer.name,
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/advice")
def generate_advice(q: QueryIn):
    reply = get_advisory(q.message, q.crop, q.city, language=q.locale)

    db = SessionLocal()
    item = QueryDB(message=q.message, reply=reply, crop=q.crop, city=q.city)
    db.add(item)
    db.commit()
    db.refresh(item)
    db.close()

    return {
        "query": q.message,
        "crop": q.crop,
        "reply": reply,
        "id": item.id,
        "language": q.locale,
    }

@app.get("/queries")
def list_queries(db: Session = Depends(get_db)):
    items = db.query(QueryDB).order_by(QueryDB.created_at.desc()).all()
    return [
        {
            "id": q.id,
            "message": q.message,
            "reply": q.reply,
            "crop": q.crop,
            "created_at": q.created_at,
            "escalated": q.escalated,
        }
        for q in items
    ]
@app.post("/queries/{query_id}/escalate")
def toggle_escalation(query_id: int, db: Session = Depends(get_db)):
    q = db.query(QueryDB).filter(QueryDB.id == query_id).first()
    if not q:
        return {"error": "Query not found"}

    q.escalated = not q.escalated
    db.commit()
    db.refresh(q)
    return {"id": q.id, "escalated": q.escalated}

# -------------------
# Extra Routes for Dashboard
# -------------------

def get_weather(city: str):
    """Fetch weather data from OpenWeatherMap API."""
    api_key = os.getenv("OPENWEATHER_KEY")
    if not api_key:
        raise Exception("OPENWEATHER_API_KEY not set in environment variables")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Weather API error: {response.text}")
    return response.json()

@app.get("/weather")
def weather_route(city: str = Query(..., description="City name to fetch weather for")):
    try:
        raw = get_weather(city)

        return {
            "city": raw.get("name"),
            "country": raw.get("sys", {}).get("country"),
            "description": raw.get("weather", [{}])[0].get("description"),
            "temperature": raw.get("main", {}).get("temp"),
            "feels_like": raw.get("main", {}).get("feels_like"),
            "humidity": raw.get("main", {}).get("humidity"),
            "pressure": raw.get("main", {}).get("pressure"),
            "wind_speed": raw.get("wind", {}).get("speed"),
        }

    except Exception as e:
        return {"error": str(e)}

# ----------------------
# Get central schemes
# ----------------------
@app.get("/schemes/central")
def central_schemes(db: Session = Depends(get_db)):
    schemes = db.query(Scheme).filter(Scheme.scheme_type == "Central").all()
    return [
        {
            "name": s.name,
            "description": s.description,
            "benefit": s.benefit,
            "apply_link": s.apply_link
        } for s in schemes
    ]

# ----------------------
# Get state schemes
# ----------------------
@app.get("/schemes/state")
def state_schemes(state: str = Query(..., description="Select your state"), db: Session = Depends(get_db)):
    schemes = db.query(Scheme).filter(Scheme.scheme_type == "State", Scheme.state == state).all()
    return [
        {
            "name": s.name,
            "description": s.description,
            "benefit": s.benefit,
            "apply_link": s.apply_link
        } for s in schemes
    ]

@app.get("/profile")
def get_profile(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    from jose import jwt, JWTError

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        farmer_id = int(payload.get("sub"))
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    farmer = db.query(Farmer).filter(Farmer.id == farmer_id).first()
    if not farmer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Farmer not found")

    return {
        "id": farmer.id,
        "name": farmer.name,
        "phone": farmer.phone,
        "location": farmer.location,
        "crops": farmer.crops,
    }

@app.get("/crops/{crop_name}")
def get_crop_info(crop_name: str):
    """
    Returns information about a specific crop.
    """
    crop_info = CROPS_DATA.get(crop_name.lower(), "Info not available")
    return {"crop": crop_name, "info": crop_info}

@app.get("/soil/{city}")
def get_soil_info(city: str):
    """
    Returns the soil type and pH value for a specific city.
    """
    city_info = SOIL_DATA.get(city.lower())
    if city_info:
        return {"city": city, "soil_type": city_info["soil_type"], "ph": city_info["ph"]}
    else:
        return {"city": city, "soil_type": "Info not available", "ph": "Info not available"}

@app.post("/detection")
def crop_detection():
    return {"status": "coming soon", "message": "YOLO crop detection will be added later."}

@app.get("/market-rates")
def get_market_rates(crop: str = None):
    """
    Returns the market rate for a specific crop or all crops.
    """
    if crop:
        rate = MARKET_RATES.get(crop.lower(), "Rate not available")
        return {crop: rate}
    return MARKET_RATES

@app.get("/fertilizer-info")
def get_fertilizer_info(name: str = None):
    fertilizers = {
        "urea": "46% nitrogen, promotes leaf growth.",
        "dap": "18% nitrogen, 46% phosphorus.",
        "mop": "60% potassium, improves drought resistance.",
    }
    if name:
        return {name: fertilizers.get(name.lower(), "Not available")}
    return fertilizers

@app.get("/irrigation/{crop_name}")
def get_irrigation(crop_name: str):
    data = {
        "wheat": "Irrigate 4–5 times during the season.",
        "rice": "Needs continuous flooding during growth.",
        "maize": "Irrigate every 10–12 days.",
    }
    return {"crop": crop_name, "irrigation": data.get(crop_name.lower(), "Info not available")}

@app.get("/loans")
def get_loans():
    return [
        {"scheme": "Kisan Credit Card (KCC)", "benefit": "Easy crop loan up to ₹3 lakh"},
        {"scheme": "NABARD Loans", "benefit": "Low interest for agri-infra projects"},
    ]
@app.get("/debug-key")
def debug_key():
    return {"OPENWEATHER_KEY": os.getenv("OPENWEATHER_KEY")}
