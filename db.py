from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MONGO_URI is not set in .env file")

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Select Database and Collection
db = client["Demo"]
collection = db["Hashini"]

print("✅ MongoDB Connected Successfully")