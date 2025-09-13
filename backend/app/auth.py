from passlib.context import CryptContext
from jose import JWTError, jwt
import os
from datetime import datetime, timedelta

# --------------------------
# JWT / Token Settings
# --------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# --------------------------
# Password Hashing Settings
# --------------------------
# Use pbkdf2_sha256 (safe and works on Windows)
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

# --------------------------
# Password Functions
# --------------------------
def hash_password(password: str) -> str:
    """
    Hashes a plain password
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a password against its hash
    """
    return pwd_context.verify(plain_password, hashed_password)

# --------------------------
# JWT Token Functions
# --------------------------
def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Creates a JWT token with expiration
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str) -> dict:
    """
    Decodes a JWT token and returns the payload
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return {}