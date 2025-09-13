from db import SessionLocal, Base, engine, Scheme

# ✅ Create tables if they don't exist
Base.metadata.create_all(bind=engine)

def seed_schemes(db):
    schemes_data = [
        # Central Govt Schemes
        {"name": "PM-Kisan", "description": "Provides ₹6,000 annually to eligible farmers.", "benefit": "₹6,000/year", "state": None, "scheme_type": "Central", "apply_link": "https://pmkisan.gov.in/"},
        {"name": "PM Fasal Bima Yojana (PMFBY)", "description": "Crop insurance for farmers against natural calamities.", "benefit": "Financial support for crop loss", "state": None, "scheme_type": "Central", "apply_link": "https://pmfby.gov.in/"},
        {"name": "PM Krishi Sinchayee Yojana (PMKSY)", "description": "Enhances irrigation coverage with 'Per Drop More Crop' initiative.", "benefit": "Subsidies for micro-irrigation systems", "state": None, "scheme_type": "Central", "apply_link": "https://pmksy.gov.in/"},
        {"name": "Kisan Credit Card (KCC)", "description": "Provides short-term credit to farmers for agricultural needs.", "benefit": "Timely access to credit", "state": None, "scheme_type": "Central", "apply_link": "https://agricoop.nic.in/kcc-scheme"},
        {"name": "Soil Health Card Scheme", "description": "Provides soil nutrient status and fertilizer recommendations.", "benefit": "Free soil testing and advisory", "state": None, "scheme_type": "Central", "apply_link": "https://soilhealth.dac.gov.in/"},
        {"name": "National Agriculture Market (e-NAM)", "description": "An online trading portal for agricultural commodities.", "benefit": "Better price realization", "state": None, "scheme_type": "Central", "apply_link": "https://enam.gov.in/web/"},
        {"name": "PM-KUSUM Scheme", "description": "Promotes the use of solar pumps for irrigation.", "benefit": "Subsidies for solar pump installation", "state": None, "scheme_type": "Central", "apply_link": "https://pmkusum.mnre.gov.in/"},
        {"name": "Mission for Integrated Development of Horticulture (MIDH)", "description": "Holistic development of the horticulture sector.", "benefit": "Subsidies for horticulture projects", "state": None, "scheme_type": "Central", "apply_link": "https://midh.gov.in/"},
        {"name": "National Livestock Mission (NLM)", "description": "Focuses on the quantitative and qualitative improvement in livestock production.", "benefit": "Support for livestock farming", "state": None, "scheme_type": "Central", "apply_link": "https://nlm.udyamimitra.in/"},
        {"name": "Pradhan Mantri Matsya Sampada Yojana (PMMSY)", "description": "A flagship scheme to bring about the Blue Revolution in India with a focus on sustainable and responsible fisheries development.", "benefit": "Support for fisheries development", "state": None, "scheme_type": "Central", "apply_link": "https://dof.gov.in/pmmsy"},
        
        # State Schemes
        # Andaman and Nicobar Islands
        {"name": "Kisan Credit Card (KCC)", "description": "Provides credit to animal husbandry farmers.", "benefit": "Credit access", "state": "Andaman and Nicobar Islands", "scheme_type": "UT", "apply_link": "https://nicobars.andaman.nic.in/schemes/"},
        {"name": "Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Andaman and Nicobar Islands", "scheme_type": "UT", "apply_link": "https://nicobars.andaman.nic.in/schemes/"},
        {"name": "Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Andaman and Nicobar Islands", "scheme_type": "UT", "apply_link": "https://nicobars.andaman.nic.in/schemes/"},
        {"name": "Horticulture Development Scheme", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Andaman and Nicobar Islands", "scheme_type": "UT", "apply_link": "https://nicobars.andaman.nic.in/schemes/"},
        {"name": "Organic Farming Scheme", "description": "Promotes organic farming practices.", "benefit": "Organic farming support", "state": "Andaman and Nicobar Islands", "scheme_type": "UT", "apply_link": "https://nicobars.andaman.nic.in/schemes/"},
        
        # Andhra Pradesh
        {"name": "Annadata Sukhibhava Scheme", "description": "Provides financial assistance to farmers.", "benefit": "₹20,000/year (state+central contribution)", "state": "Andhra Pradesh", "scheme_type": "State", "apply_link": "https://tdpschemes.com/annadata-sukhibhava-scheme/"},
        {"name": "YSR Jala Siri", "description": "Irrigation support for farmers.", "benefit": "Irrigation support", "state": "Andhra Pradesh", "scheme_type": "State", "apply_link": "https://jala-siri.ap.gov.in/"},
        {"name": "YSR Sunna Vaddi", "description": "Interest-free crop loan scheme.", "benefit": "Interest-free loan", "state": "Andhra Pradesh", "scheme_type": "State", "apply_link": "https://ysrsunnavaddi.ap.gov.in/"},
        {"name": "YSR Rythu Seva", "description": "Crop insurance scheme.", "benefit": "Crop insurance", "state": "Andhra Pradesh", "scheme_type": "State", "apply_link": "https://ysrrythuseva.ap.gov.in/"},
        {"name": "AP Crop Insurance Scheme", "description": "Provides insurance for crops.", "benefit": "Crop insurance", "state": "Andhra Pradesh", "scheme_type": "State", "apply_link": "https://apcropinsurance.ap.gov.in/"},

        # Arunachal Pradesh
        {"name": "Atma Nirbhar Bagwani Yojana", "description": "An umbrella scheme to promote horticulture through a bank-linked credit subsidy model.", "benefit": "45% subsidy, 45% bank loan, 10% beneficiary contribution", "state": "Arunachal Pradesh", "scheme_type": "State", "apply_link": "https://www.myscheme.gov.in/schemes/anby"},
        {"name": "Chief Minister's Krishi Rinn Yojana", "description": "Provides a zero-interest crop loan facility for farmers.", "benefit": "Zero interest crop loan", "state": "Arunachal Pradesh", "scheme_type": "State", "apply_link": "https://kurungkumey.nic.in/scheme/chief-ministers-krishi-rinn-yojana/"},
        {"name": "Arunachal Pradesh Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Arunachal Pradesh", "scheme_type": "State", "apply_link": "https://agri.arunachal.gov.in/"},
        {"name": "Arunachal Pradesh Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Arunachal Pradesh", "scheme_type": "State", "apply_link": "https://agri.arunachal.gov.in/"},
        {"name": "Arunachal Pradesh Horticulture Development Scheme", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Arunachal Pradesh", "scheme_type": "State", "apply_link": "https://agri.arunachal.gov.in/"},
        
        # Assam
        {"name": "Assam Farmer's Credit Subsidy Scheme", "description": "Offers partial crop loan waiver to farmers.", "benefit": "25% loan waiver (max ₹25,000)", "state": "Assam", "scheme_type": "State", "apply_link": "https://www.indiafilings.com/learn/assam-farmers-credit-subsidy-scheme/"},
        {"name": "Assam Orunodoi Scheme", "description": "Financial assistance to low-income families.", "benefit": "Financial assistance", "state": "Assam", "scheme_type": "State", "apply_link": "https://orunodoi.assam.gov.in/"},
        {"name": "Assam Kisan Credit Card Scheme", "description": "Provides credit to farmers.", "benefit": "Credit access", "state": "Assam", "scheme_type": "State", "apply_link": "https://agri.assam.gov.in/"},
        {"name": "Assam Seed Certification Scheme", "description": "Ensures quality seed production.", "benefit": "Seed certification", "state": "Assam", "scheme_type": "State", "apply_link": "https://agri.assam.gov.in/"},
        {"name": "Assam Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Assam", "scheme_type": "State", "apply_link": "https://agri.assam.gov.in/"},
        
        # Bihar
        {"name": "Bihar Rajya Fasal Sahayata Yojana", "description": "State-level crop insurance scheme that provides financial assistance for crop losses.", "benefit": "Financial aid for crop loss", "state": "Bihar", "scheme_type": "State", "apply_link": "https://esahkari.bihar.gov.in/"},
        {"name": "Mukhyamantri Nijee Nalkoop Yojana", "description": "Provides assistance for installing private tubewells.", "benefit": "Tubewell subsidy", "state": "Bihar", "scheme_type": "State", "apply_link": "http://mwrd.bihar.gov.in/"},
        {"name": "Agricultural Mechanization Scheme", "description": "Offers subsidies on various farm machinery and equipment.", "benefit": "Farm machinery subsidy", "state": "Bihar", "scheme_type": "State", "apply_link": "http://farmech.bihar.gov.in/"},
        {"name": "Mukhyamantri Bagwani Mission", "description": "Promotes commercial horticulture.", "benefit": "Horticulture development support", "state": "Bihar", "scheme_type": "State", "apply_link": "https://horticulture.bihar.gov.in/"},
        {"name": "Bihar Kisan Samman Nidhi", "description": "Financial support to farmers.", "benefit": "Financial support", "state": "Bihar", "scheme_type": "State", "apply_link": "https://dbtagriculture.bihar.gov.in/"},
        
        # Chandigarh
        {"name": "Extension and Farmers Training Study Tour", "description": "Acquaints farmers with the latest and improved farming techniques through study tours.", "benefit": "Training and exposure", "state": "Chandigarh", "scheme_type": "UT", "apply_link": "https://chandigarh.gov.in/departments/other-departments/agriculture"},
        {"name": "Organic Cultivation of Seeds & Horticulture", "description": "Supports and promotes organic cultivation of seeds and horticulture.", "benefit": "Organic farming support", "state": "Chandigarh", "scheme_type": "UT", "apply_link": "https://chandigarh.gov.in/departments/other-departments/agriculture"},
        {"name": "Chandigarh Kisan Samman Nidhi", "description": "Financial support to farmers.", "benefit": "Financial support", "state": "Chandigarh", "scheme_type": "UT", "apply_link": "https://chandigarh.gov.in/"},
        {"name": "Chandigarh Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Chandigarh", "scheme_type": "UT", "apply_link": "https://chandigarh.gov.in/"},
        {"name": "Chandigarh Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Chandigarh", "scheme_type": "UT", "apply_link": "https://chandigarh.gov.in/"},
        
        # Chhattisgarh
        {"name": "Krishak Unnati Yojana", "description": "Direct incentive scheme to promote crop diversification and reduce dependence on paddy.", "benefit": "₹10,000-₹11,000 per acre financial assistance", "state": "Chhattisgarh", "scheme_type": "State", "apply_link": "https://manendragarh-chirmiri-bharatpur.cg.gov.in/en/scheme/unified-farmer-portal-ufp/"},
        {"name": "Rajiv Gandhi Kisan Nyay Yojana", "description": "Income support to farmers.", "benefit": "Income support", "state": "Chhattisgarh", "scheme_type": "State", "apply_link": "https://rkny.cg.nic.in/"},
        {"name": "Ghanshyam Singh Gupt Kisan Kalyan Yojana", "description": "Financial assistance to farmers.", "benefit": "Financial assistance", "state": "Chhattisgarh", "scheme_type": "State", "apply_link": "https://agriportal.cg.nic.in/"},
        {"name": "Chhattisgarh Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Chhattisgarh", "scheme_type": "State", "apply_link": "https://agriportal.cg.nic.in/"},
        {"name": "Chhattisgarh Horticulture Development Scheme", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Chhattisgarh", "scheme_type": "State", "apply_link": "https://agriportal.cg.nic.in/"},
        
        # Dadra and Nagar Haveli and Daman and Diu
        {"name": "Food Processing Scheme", "description": "Supports and promotes food processing industries.", "benefit": "Support for food processing", "state": "Dadra and Nagar Haveli and Daman and Diu", "scheme_type": "UT", "apply_link": "https://dnh.gov.in/"},
        {"name": "Kisan Samman Nidhi", "description": "Financial support to farmers.", "benefit": "Financial support", "state": "Dadra and Nagar Haveli and Daman and Diu", "scheme_type": "UT", "apply_link": "https://dnh.gov.in/"},
        {"name": "Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "Dadra and Nagar Haveli and Daman and Diu", "scheme_type": "UT", "apply_link": "https://dnh.gov.in/"},
        {"name": "Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Dadra and Nagar Haveli and Daman and Diu", "scheme_type": "UT", "apply_link": "https://dnh.gov.in/"},
        {"name": "Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Dadra and Nagar Haveli and Daman and Diu", "scheme_type": "UT", "apply_link": "https://dnh.gov.in/"},
        
        # Delhi
        {"name": "Paramparagat Krishi Vikas Yojana (PKVY)", "description": "A centrally sponsored scheme promoting organic farming.", "benefit": "Support for organic farming", "state": "Delhi", "scheme_type": "UT", "apply_link": "https://dmsouthwest.delhi.gov.in/scheme/paramparagat-krishi-vikas-yojana/"},
        {"name": "Delhi Kisan Samman Nidhi", "description": "Financial support to farmers.", "benefit": "Financial support", "state": "Delhi", "scheme_type": "UT", "apply_link": "https://delhi.gov.in/"},
        {"name": "Delhi Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "Delhi", "scheme_type": "UT", "apply_link": "https://delhi.gov.in/"},
        {"name": "Delhi Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Delhi", "scheme_type": "UT", "apply_link": "https://delhi.gov.in/"},
        {"name": "Delhi Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Delhi", "scheme_type": "UT", "apply_link": "https://delhi.gov.in/"},
        
        # Goa
        {"name": "Development of Manures and Fertilizers", "description": "Provides subsidies for the use of soil conditioners, micronutrients, and for the construction of organic manure and biogas units.", "benefit": "Up to 90% subsidy on specific components", "state": "Goa", "scheme_type": "State", "apply_link": "https://goaprintingpress.gov.in/downloads/2526/2526-22-SI-OG.pdf"},
        {"name": "Goa Kisan Credit Card Scheme", "description": "Provides credit to farmers.", "benefit": "Credit access", "state": "Goa", "scheme_type": "State", "apply_link": "https://agri.goa.gov.in/"},
        {"name": "Goa Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "Goa", "scheme_type": "State", "apply_link": "https://agri.goa.gov.in/"},
        {"name": "Goa Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Goa", "scheme_type": "State", "apply_link": "https://agri.goa.gov.in/"},
        {"name": "Goa Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Goa", "scheme_type": "State", "apply_link": "https://agri.goa.gov.in/"},
        
        # Gujarat
        {"name": "Gujarat Kisan Suryoday Yojana", "description": "Day-time electricity supply for agriculture.", "benefit": "Day-time power supply", "state": "Gujarat", "scheme_type": "State", "apply_link": "https://ggrc.gujarat.gov.in/"},
        {"name": "Saat Pagla Khedut Kalyan Yojana", "description": "7 schemes for agriculture and farmer welfare.", "benefit": "Welfare support", "state": "Gujarat", "scheme_type": "State", "apply_link": "https://ikhedut.gujarat.gov.in/"},
        {"name": "Gujarat Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Gujarat", "scheme_type": "State", "apply_link": "https://ikhedut.gujarat.gov.in/"},
        {"name": "Gujarat Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Gujarat", "scheme_type": "State", "apply_link": "https://ikhedut.gujarat.gov.in/"},
        {"name": "Gujarat Horticulture Development Scheme", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Gujarat", "scheme_type": "State", "apply_link": "https://ikhedut.gujarat.gov.in/"},
        
        # Haryana
        {"name": "Mukhyamantri Kisan Samriddhi Yojana", "description": "Subsidies for solar pumps.", "benefit": "Solar pump subsidy", "state": "Haryana", "scheme_type": "State", "apply_link": "https://hareda.gov.in/en/schemes/mkpy"},
        {"name": "Bhavantar Bharpai Yojana", "description": "Price protection for fruits and vegetables.", "benefit": "Price support", "state": "Haryana", "scheme_type": "State", "apply_link": "https://fasal.haryana.gov.in/"},
        {"name": "Haryana Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Haryana", "scheme_type": "State", "apply_link": "https://fasal.haryana.gov.in/"},
        {"name": "Haryana Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Haryana", "scheme_type": "State", "apply_link": "https://fasal.haryana.gov.in/"},
        {"name": "Haryana Horticulture Development Scheme", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Haryana", "scheme_type": "State", "apply_link": "https://fasal.haryana.gov.in/"},
        
        # Himachal Pradesh
        {"name": "Mukhyamantri Khet Sanrakshan Yojana", "description": "Provides subsidy for solar fencing.", "benefit": "Solar fencing subsidy", "state": "Himachal Pradesh", "scheme_type": "State", "apply_link": "https://hpagrisnet.gov.in/"},
        {"name": "Jal Se Krishi Ko Bal", "description": "Provides support for irrigation through check dams and lift irrigation.", "benefit": "Irrigation infrastructure support", "state": "Himachal Pradesh", "scheme_type": "State", "apply_link": "https://hpagrisnet.gov.in/"},
        {"name": "Himachal Pradesh Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Himachal Pradesh", "scheme_type": "State", "apply_link": "https://hpagrisnet.gov.in/"},
        {"name": "Himachal Pradesh Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Himachal Pradesh", "scheme_type": "State", "apply_link": "https://hpagrisnet.gov.in/"},
        {"name": "Himachal Pradesh Horticulture Development Scheme", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Himachal Pradesh", "scheme_type": "State", "apply_link": "https://hpagrisnet.gov.in/"},
        
        # Jharkhand
        {"name": "Jharkhand Kisan Samriddhi Yojana", "description": "Assistance for solar-powered irrigation systems.", "benefit": "Solar irrigation subsidy", "state": "Jharkhand", "scheme_type": "State", "apply_link": "https://jharkhand.gov.in/"},
        {"name": "Jharkhand Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "Jharkhand", "scheme_type": "State", "apply_link": "https://jharkhand.gov.in/"},
        {"name": "Jharkhand Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Jharkhand", "scheme_type": "State", "apply_link": "https://jharkhand.gov.in/"},
        {"name": "Jharkhand Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Jharkhand", "scheme_type": "State", "apply_link": "https://jharkhand.gov.in/"},
        {"name": "Jharkhand Horticulture Development Scheme", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Jharkhand", "scheme_type": "State", "apply_link": "https://jharkhand.gov.in/"},
        
        # Jammu and Kashmir
        {"name": "Fisheries Department Schemes", "description": "Provides assistance for the construction of new carp ponds and trout raceways.", "benefit": "Fisheries support", "state": "Jammu and Kashmir", "scheme_type": "UT", "apply_link": "https://jkgov.in/"},
        {"name": "Jammu and Kashmir Kisan Samman Nidhi", "description": "Financial support to farmers.", "benefit": "Financial support", "state": "Jammu and Kashmir", "scheme_type": "UT", "apply_link": "https://jkgov.in/"},
        {"name": "Jammu and Kashmir Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "Jammu and Kashmir", "scheme_type": "UT", "apply_link": "https://jkgov.in/"},
        {"name": "Jammu and Kashmir Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Jammu and Kashmir", "scheme_type": "UT", "apply_link": "https://jkgov.in/"},
        {"name": "Jammu and Kashmir Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Jammu and Kashmir", "scheme_type": "UT", "apply_link": "https://jkgov.in/"},
        
        # Karnataka
        {"name": "Raitha Vidya Nidhi", "description": "Scholarship for farmers' children.", "benefit": "Scholarship", "state": "Karnataka", "scheme_type": "State", "apply_link": "https://raitamitra.karnataka.gov.in/"},
        {"name": "Raitha Shakthi", "description": "Diesel subsidy for farm machinery.", "benefit": "Diesel subsidy", "state": "Karnataka", "scheme_type": "State", "apply_link": "https://raitamitra.karnataka.gov.in/"},
        {"name": "Savayava Siri", "description": "Promotes organic farming.", "benefit": "Organic farming support", "state": "Karnataka", "scheme_type": "State", "apply_link": "https://raitamitra.karnataka.in/"},
        {"name": "Organic Carbon Mission", "description": "An initiative to increase organic carbon in the soil.", "benefit": "Soil health improvement", "state": "Karnataka", "scheme_type": "State", "apply_link": "https://raitamitra.karnataka.gov.in/"},
        {"name": "Karnataka Kisan Samman Nidhi", "description": "Financial support to farmers.", "benefit": "Financial support", "state": "Karnataka", "scheme_type": "State", "apply_link": "https://raitamitra.karnataka.gov.in/"},
        
        # Kerala
        {"name": "Krishi Bhavan Scheme", "description": "Support for various agricultural activities.", "benefit": "Agricultural support", "state": "Kerala", "scheme_type": "State", "apply_link": "https://www.keralaagriculture.gov.in/"},
        {"name": "Krishi Vikas Yojana", "description": "Supports crop diversification and farm mechanization.", "benefit": "Financial support", "state": "Kerala", "scheme_type": "State", "apply_link": "https://www.keralaagriculture.gov.in/"},
        {"name": "Kerala Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Kerala", "scheme_type": "State", "apply_link": "https://www.keralaagriculture.gov.in/"},
        {"name": "Kerala Horticulture Development Scheme", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Kerala", "scheme_type": "State", "apply_link": "https://www.keralaagriculture.gov.in/"},
        {"name": "Kerala Organic Farming Scheme", "description": "Promotes organic farming practices.", "benefit": "Organic farming support", "state": "Kerala", "scheme_type": "State", "apply_link": "https://www.keralaagriculture.gov.in/"},
        
        # Ladakh
        {"name": "Ladakh Agriculture Extension (ATMA) Scheme", "description": "Disseminates scientific technologies to increase crop production.", "benefit": "Technology dissemination", "state": "Ladakh", "scheme_type": "UT", "apply_link": "https://ladakh.gov.in/agriculture/"},
        {"name": "Mission for Integrated Development of Horticulture (MIDH)", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Ladakh", "scheme_type": "UT", "apply_link": "https://ladakh.gov.in/agriculture/"},
        {"name": "Per Drop More Crop (PDMC)", "description": "Promotes micro-irrigation systems.", "benefit": "Micro-irrigation support", "state": "Ladakh", "scheme_type": "UT", "apply_link": "https://ladakh.gov.in/agriculture/"},
        {"name": "Paramparagat Krishi Vikas Yojana (PKVY)", "description": "Supports organic farming.", "benefit": "Organic farming support", "state": "Ladakh", "scheme_type": "UT", "apply_link": "https://ladakh.gov.in/agriculture/"},
        {"name": "Sub-Mission on Agricultural Mechanization (SMAM)", "description": "Promotes farm mechanization.", "benefit": "Farm mechanization support", "state": "Ladakh", "scheme_type": "UT", "apply_link": "https://ladakh.gov.in/agriculture/"},
        
        # Lakshadweep
        {"name": "Nutri Garden Scheme", "description": "Encourages terrace and backyard cultivation of vegetables and fruits.", "benefit": "Home gardening support", "state": "Lakshadweep", "scheme_type": "UT", "apply_link": "https://lakshadweep.gov.in/departments/agriculture/"},
        {"name": "Coconut Development Programme", "description": "Provides farm inputs for coconut cultivation.", "benefit": "Coconut cultivation support", "state": "Lakshadweep", "scheme_type": "UT", "apply_link": "https://lakshadweep.gov.in/departments/agriculture/"},
        {"name": "Lakshadweep Kisan Samman Nidhi", "description": "Financial support to farmers.", "benefit": "Financial support", "state": "Lakshadweep", "scheme_type": "UT", "apply_link": "https://lakshadweep.gov.in/"},
        {"name": "Lakshadweep Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Lakshadweep", "scheme_type": "UT", "apply_link": "https://lakshadweep.gov.in/"},
        {"name": "Lakshadweep Horticulture Development Scheme", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Lakshadweep", "scheme_type": "UT", "apply_link": "https://lakshadweep.gov.in/"},
        
        # Madhya Pradesh
        {"name": "Mukhyamantri Kisan Kalyan Yojana", "description": "Direct income support to farmers.", "benefit": "Income support", "state": "Madhya Pradesh", "scheme_type": "State", "apply_link": "https://www.mp.gov.in/"},
        {"name": "Bhavantar Bhugtan Yojana", "description": "Compensates farmers for the price difference when crops are sold below MSP.", "benefit": "Market price support", "state": "Madhya Pradesh", "scheme_type": "State", "apply_link": "https://mpbhavantar.nic.in/"},
        {"name": "MP Fal Podharopan Yojana", "description": "Provides subsidies for fruit cultivation.", "benefit": "Fruit cultivation subsidy", "state": "Madhya Pradesh", "scheme_type": "State", "apply_link": "https://mpfsts.mp.gov.in/"},
        {"name": "MP Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Madhya Pradesh", "scheme_type": "State", "apply_link": "https://mpfsts.mp.gov.in/"},
        {"name": "MP Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Madhya Pradesh", "scheme_type": "State", "apply_link": "https://mpfsts.mp.gov.in/"},
        
        # Maharashtra
        {"name": "Maha Krishi Samrudhi Yojana", "description": "Loan for food and agro-based industries.", "benefit": "Loan access", "state": "Maharashtra", "scheme_type": "State", "apply_link": "https://bankofmaharashtra.in/"},
        {"name": "Jalyukt Shivar Abhiyan", "description": "Creating water conservation structures.", "benefit": "Water conservation support", "state": "Maharashtra", "scheme_type": "State", "apply_link": "https://jalyuktshivar.maharashtra.gov.in/"},
        {"name": "Mahabank Kisan Credit Card", "description": "Provides credit to animal husbandry and fisheries farmers.", "benefit": "Credit access", "state": "Maharashtra", "scheme_type": "State", "apply_link": "https://bankofmaharashtra.in/"},
        {"name": "Maharashtra Agri-machinery Rental Scheme", "description": "Provides farm machinery for rent.", "benefit": "Machinery rental", "state": "Maharashtra", "scheme_type": "State", "apply_link": "https://agri.maharashtra.gov.in/"},
        {"name": "Maharashtra Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Maharashtra", "scheme_type": "State", "apply_link": "https://agri.maharashtra.gov.in/"},
        
        # Manipur
        {"name": "Chief Minister's Farmer Livelihood Support Scheme", "description": "Support for agriculture-based livelihoods.", "benefit": "Livelihood support", "state": "Manipur", "scheme_type": "State", "apply_link": "https://manipur.gov.in/"},
        {"name": "Manipur Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "Manipur", "scheme_type": "State", "apply_link": "https://manipur.gov.in/"},
        {"name": "Manipur Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Manipur", "scheme_type": "State", "apply_link": "https://manipur.gov.in/"},
        {"name": "Manipur Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Manipur", "scheme_type": "State", "apply_link": "https://manipur.gov.in/"},
        {"name": "Manipur Horticulture Development Scheme", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Manipur", "scheme_type": "State", "apply_link": "https://manipur.gov.in/"},
        
        # Meghalaya
        {"name": "State Rice Mission", "description": "Aims to increase rice productivity.", "benefit": "Productivity support", "state": "Meghalaya", "scheme_type": "State", "apply_link": "https://www.megagriculture.gov.in/"},
        {"name": "Meghalaya Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "Meghalaya", "scheme_type": "State", "apply_link": "https://www.megagriculture.gov.in/"},
        {"name": "Meghalaya Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Meghalaya", "scheme_type": "State", "apply_link": "https://www.megagriculture.gov.in/"},
        {"name": "Meghalaya Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Meghalaya", "scheme_type": "State", "apply_link": "https://www.megagriculture.gov.in/"},
        {"name": "Meghalaya Horticulture Development Scheme", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Meghalaya", "scheme_type": "State", "apply_link": "https://www.megagriculture.gov.in/"},
        
        # Mizoram
        {"name": "Mizoram Organic Farming Scheme", "description": "Promotes and provides assistance for organic farming.", "benefit": "Organic farming support", "state": "Mizoram", "scheme_type": "State", "apply_link": "https://www.agrimizoram.nic.in/"},
        {"name": "Mizoram Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "Mizoram", "scheme_type": "State", "apply_link": "https://www.agrimizoram.nic.in/"},
        {"name": "Mizoram Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Mizoram", "scheme_type": "State", "apply_link": "https://www.agrimizoram.nic.in/"},
        {"name": "Mizoram Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Mizoram", "scheme_type": "State", "apply_link": "https://www.agrimizoram.nic.in/"},
        {"name": "Mizoram Horticulture Development Scheme", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Mizoram", "scheme_type": "State", "apply_link": "https://www.agrimizoram.nic.in/"},
        
        # Nagaland
        {"name": "Chief Minister's Micro Finance Initiative", "description": "Bank credit-linked subsidy for agriculture.", "benefit": "Credit subsidy", "state": "Nagaland", "scheme_type": "State", "apply_link": "https://www.myscheme.gov.in/schemes/cmmfi"},
        {"name": "Nagaland Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "Nagaland", "scheme_type": "State", "apply_link": "https://nagaland.gov.in/"},
        {"name": "Nagaland Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Nagaland", "scheme_type": "State", "apply_link": "https://nagaland.gov.in/"},
        {"name": "Nagaland Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Nagaland", "scheme_type": "State", "apply_link": "https://nagaland.gov.in/"},
        {"name": "Nagaland Horticulture Development Scheme", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Nagaland", "scheme_type": "State", "apply_link": "https://nagaland.gov.in/"},

        # Odisha
        {"name": "Kalia Scheme", "description": "Financial assistance to small and marginal farmers.", "benefit": "Financial assistance", "state": "Odisha", "scheme_type": "State", "apply_link": "https://kalia.odisha.gov.in/"},
        {"name": "Odisha Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "Odisha", "scheme_type": "State", "apply_link": "https://odisha.gov.in/"},
        {"name": "Odisha Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Odisha", "scheme_type": "State", "apply_link": "https://odisha.gov.in/"},
        {"name": "Odisha Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Odisha", "scheme_type": "State", "apply_link": "https://odisha.gov.in/"},
        {"name": "Odisha Horticulture Development Scheme", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Odisha", "scheme_type": "State", "apply_link": "https://odisha.gov.in/"},

        # Puducherry
        {"name": "FPO Financial Support Scheme", "description": "Provides one-time financial assistance to Farmer Producer Organizations.", "benefit": "Financial assistance", "state": "Puducherry", "scheme_type": "UT", "apply_link": "https://puducherry-dt.gov.in/"},
        {"name": "Puducherry Kisan Samman Nidhi", "description": "Financial support to farmers.", "benefit": "Financial support", "state": "Puducherry", "scheme_type": "UT", "apply_link": "https://puducherry-dt.gov.in/"},
        {"name": "Puducherry Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "Puducherry", "scheme_type": "UT", "apply_link": "https://puducherry-dt.gov.in/"},
        {"name": "Puducherry Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Puducherry", "scheme_type": "UT", "apply_link": "https://puducherry-dt.gov.in/"},
        {"name": "Puducherry Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Puducherry", "scheme_type": "UT", "apply_link": "https://puducherry-dt.gov.in/"},
        
        # Punjab
        {"name": "Punjab Kisan Samman Nidhi", "description": "Financial support to farmers.", "benefit": "Financial support", "state": "Punjab", "scheme_type": "State", "apply_link": "https://punjab.gov.in/"},
        {"name": "Punjab Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "Punjab", "scheme_type": "State", "apply_link": "https://punjab.gov.in/"},
        {"name": "Punjab Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Punjab", "scheme_type": "State", "apply_link": "https://punjab.gov.in/"},
        {"name": "Punjab Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Punjab", "scheme_type": "State", "apply_link": "https://punjab.gov.in/"},
        {"name": "Punjab Horticulture Development Scheme", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Punjab", "scheme_type": "State", "apply_link": "https://punjab.gov.in/"},
        
        # Rajasthan
        {"name": "Mukhyamantri Krishak Sathi Yojana", "description": "Financial assistance for various agricultural activities.", "benefit": "Financial assistance", "state": "Rajasthan", "scheme_type": "State", "apply_link": "https://rajras.in/ras/pre/rajasthan/adm/schemes/"},
        {"name": "Mukhyamantri Beej Swavalamban Yojana", "description": "Supports farmers in producing their own quality seeds.", "benefit": "Seed production support", "state": "Rajasthan", "scheme_type": "State", "apply_link": "https://rajras.in/ras/pre/rajasthan/adm/schemes/"},
        {"name": "Rajasthan Krishak Rin Mafi Yojana", "description": "Provides a loan waiver for farmers.", "benefit": "Loan waiver", "state": "Rajasthan", "scheme_type": "State", "apply_link": "https://rajras.in/ras/pre/rajasthan/adm/schemes/"},
        {"name": "Rajeev Gandhi Krishak Sathi Sahayata Yojana", "description": "Financial assistance for farmers, laborers, and traders in the mandi.", "benefit": "Financial assistance", "state": "Rajasthan", "scheme_type": "State", "apply_link": "https://rajras.in/ras/pre/rajasthan/adm/schemes/"},
        {"name": "Rajasthan Kisan Credit Card Scheme", "description": "Provides credit to farmers.", "benefit": "Credit access", "state": "Rajasthan", "scheme_type": "State", "apply_link": "https://rajras.in/ras/pre/rajasthan/adm/schemes/"},
        
        # Sikkim
        {"name": "Sikkim Organic Mission", "description": "Promotes and supports organic farming practices.", "benefit": "Organic farming support", "state": "Sikkim", "scheme_type": "State", "apply_link": "https://sikkim.gov.in/"},
        {"name": "Sikkim Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "Sikkim", "scheme_type": "State", "apply_link": "https://sikkim.gov.in/"},
        {"name": "Sikkim Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Sikkim", "scheme_type": "State", "apply_link": "https://sikkim.gov.in/"},
        {"name": "Sikkim Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Sikkim", "scheme_type": "State", "apply_link": "https://sikkim.gov.in/"},
        {"name": "Sikkim Horticulture Development Scheme", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Sikkim", "scheme_type": "State", "apply_link": "https://sikkim.gov.in/"},
        
        # Tamil Nadu
        {"name": "Chief Minister's Solar Powered Pumpset Scheme", "description": "Provides subsidies for solar pumps for irrigation.", "benefit": "Solar pump subsidy", "state": "Tamil Nadu", "scheme_type": "State", "apply_link": "https://www.agri.tn.gov.in/"},
        {"name": "Tamil Nadu Kisan Samman Nidhi", "description": "Financial support to farmers.", "benefit": "Financial support", "state": "Tamil Nadu", "scheme_type": "State", "apply_link": "https://www.agri.tn.gov.in/"},
        {"name": "Tamil Nadu Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "Tamil Nadu", "scheme_type": "State", "apply_link": "https://www.agri.tn.gov.in/"},
        {"name": "Tamil Nadu Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Tamil Nadu", "scheme_type": "State", "apply_link": "https://www.agri.tn.gov.in/"},
        {"name": "Tamil Nadu Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Tamil Nadu", "scheme_type": "State", "apply_link": "https://www.agri.tn.gov.in/"},
        
        # Telangana
        {"name": "Rythu Bandhu", "description": "Provides financial assistance for crop investment.", "benefit": "₹5,000/acre per season", "state": "Telangana", "scheme_type": "State", "apply_link": "https://rythubandhu.telangana.gov.in/"},
        {"name": "Rythu Bima", "description": "Life insurance scheme for farmers.", "benefit": "₹5 lakh life insurance", "state": "Telangana", "scheme_type": "State", "apply_link": "https://rythubima.telangana.gov.in/"},
        {"name": "Telangana Kisan Samman Nidhi", "description": "Financial support to farmers.", "benefit": "Financial support", "state": "Telangana", "scheme_type": "State", "apply_link": "https://telangana.gov.in/"},
        {"name": "Telangana Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "Telangana", "scheme_type": "State", "apply_link": "https://telangana.gov.in/"},
        {"name": "Telangana Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Telangana", "scheme_type": "State", "apply_link": "https://telangana.gov.in/"},
        
        # Tripura
        {"name": "Tripura Kisan Samman Nidhi", "description": "Financial support to farmers.", "benefit": "Financial support", "state": "Tripura", "scheme_type": "State", "apply_link": "https://tripura.gov.in/"},
        {"name": "Tripura Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "Tripura", "scheme_type": "State", "apply_link": "https://tripura.gov.in/"},
        {"name": "Tripura Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Tripura", "scheme_type": "State", "apply_link": "https://tripura.gov.in/"},
        {"name": "Tripura Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Tripura", "scheme_type": "State", "apply_link": "https://tripura.gov.in/"},
        {"name": "Tripura Horticulture Development Scheme", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Tripura", "scheme_type": "State", "apply_link": "https://tripura.gov.in/"},
        
        # Uttar Pradesh
        {"name": "Mukhyamantri Khet Suraksha Yojana", "description": "Provides financial assistance for solar fencing to protect crops.", "benefit": "Solar fencing subsidy", "state": "Uttar Pradesh", "scheme_type": "State", "apply_link": "https://upagripardarshi.gov.in/"},
        {"name": "UP Kisan Samman Nidhi", "description": "Financial support to farmers.", "benefit": "Financial support", "state": "Uttar Pradesh", "scheme_type": "State", "apply_link": "https://upagripardarshi.gov.in/"},
        {"name": "UP Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "Uttar Pradesh", "scheme_type": "State", "apply_link": "https://upagripardarshi.gov.in/"},
        {"name": "UP Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Uttar Pradesh", "scheme_type": "State", "apply_link": "https://upagripardarshi.gov.in/"},
        {"name": "UP Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Uttar Pradesh", "scheme_type": "State", "apply_link": "https://upagripardarshi.gov.in/"},
        
        # Uttarakhand
        {"name": "Uttarakhand Kisan Samman Nidhi", "description": "Financial support to farmers.", "benefit": "Financial support", "state": "Uttarakhand", "scheme_type": "State", "apply_link": "https://uk.gov.in/"},
        {"name": "Uttarakhand Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "Uttarakhand", "scheme_type": "State", "apply_link": "https://uk.gov.in/"},
        {"name": "Uttarakhand Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "Uttarakhand", "scheme_type": "State", "apply_link": "https://uk.gov.in/"},
        {"name": "Uttarakhand Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "Uttarakhand", "scheme_type": "State", "apply_link": "https://uk.gov.in/"},
        {"name": "Uttarakhand Horticulture Development Scheme", "description": "Supports horticulture development.", "benefit": "Horticulture development support", "state": "Uttarakhand", "scheme_type": "State", "apply_link": "https://uk.gov.in/"},
        
        # West Bengal
        {"name": "Krishak Bandhu", "description": "Provides financial assistance for crop investment and death benefits to farmers.", "benefit": "₹10,000/acre annually", "state": "West Bengal", "scheme_type": "State", "apply_link": "https://krishakbandhu.net/"},
        {"name": "West Bengal Kisan Samman Nidhi", "description": "Financial support to farmers.", "benefit": "Financial support", "state": "West Bengal", "scheme_type": "State", "apply_link": "https://wbagri.gov.in/"},
        {"name": "West Bengal Seed Certification Scheme", "description": "Quality seed certification.", "benefit": "Seed certification", "state": "West Bengal", "scheme_type": "State", "apply_link": "https://wbagri.gov.in/"},
        {"name": "West Bengal Crop Insurance Scheme", "description": "Crop insurance for farmers.", "benefit": "Crop insurance", "state": "West Bengal", "scheme_type": "State", "apply_link": "https://wbagri.gov.in/"},
        {"name": "West Bengal Irrigation Scheme", "description": "Irrigation facilities for farmers.", "benefit": "Irrigation support", "state": "West Bengal", "scheme_type": "State", "apply_link": "https://wbagri.gov.in/"}
    ]

    for s in schemes_data:
        if not db.query(Scheme).filter(Scheme.name == s["name"]).first():
            db.add(Scheme(**s))
    db.commit()
    print("✅ Schemes seeded successfully!")

# ✅ Main execution
if __name__ == "__main__":
    db = SessionLocal()
    seed_schemes(db)
    db.close()
    print("✅ Seeding completed.")