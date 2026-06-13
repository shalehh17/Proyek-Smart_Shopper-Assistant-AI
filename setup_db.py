from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Initialize environment variables for database connectivity
load_dotenv()

# Establish connection to MongoDB cluster
client = MongoClient(os.getenv("MONGO_URI"))
db = client["smart_shopper_db"]
collection = db["common_info"]

# Define target dataset for knowledge base ingestion
data = [
  {"topic": "Pengiriman", "keywords": ["pengiriman", "lama", "estimasi", "sampai", "ekspedisi"], "answer": "Estimasi pengiriman reguler adalah 2-4 hari kerja tergantung lokasi."},
  {"topic": "Refund", "keywords": ["refund", "pengembalian", "dana", "batal", "uang"], "answer": "Proses refund dilakukan maksimal 7 hari kerja setelah barang diterima kembali."},
  {"topic": "Pembayaran", "keywords": ["pembayaran", "metode", "transfer", "bank", "bayar"], "answer": "Kami menerima transfer bank, E-Wallet, dan Virtual Account."}
]

# Purge legacy data to ensure schema consistency and data integrity
collection.delete_many({})

# Load processed dataset into the collection via bulk insertion
collection.insert_many(data)
B
# Optimize query performance by building text indexes on key features
collection.create_index([("topic", "text"), ("keywords", "text")])

print("Database state successfully synchronized with updated schema.")
