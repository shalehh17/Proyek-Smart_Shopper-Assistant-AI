import pandas as pd
import os
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv

# 1. Memuat variabel dari file .env
load_dotenv()

# 2. Ambil URI dari .env
mongo_uri = os.getenv("MONGO_URI")

# 3. Hubungkan ke MongoDB menggunakan certifi untuk sertifikat SSL yang valid
ca = certifi.where()
client = MongoClient(
    mongo_uri, 
    tls=True, 
    tlsCAFile=ca, 
    tlsAllowInvalidCertificates=False
)

db = client["smart_shopper_db"] 
collection = db["common_info"]

def upload_data():
    file_path = 'data/common_info.json'
    
    try:
        # Gunakan Pandas untuk membaca JSON
        df = pd.read_json(file_path, encoding='utf-8')
        data = df.to_dict(orient='records')
        
        # Operasi Database
        collection.delete_many({})  
        collection.drop_indexes()    
        collection.insert_many(data) 
        
        # Strategi: Membuat Text Index
        collection.create_index([("keywords", "text")])
        
        print("Data berhasil diunggah menggunakan Pandas dan Text Index berhasil dibuat!")
        
    except FileNotFoundError:
        print(f"Error: File di {file_path} tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengunggah data: {e}")

if __name__ == "__main__":
    upload_data()