import os
import certifi
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

# Environment configuration: Load credentials for secure database access
load_dotenv()

# Database connectivity: Initialize MongoDB client with TLS verification
mongo_uri = os.getenv("MONGO_URI")
ca = certifi.where()
client = MongoClient(mongo_uri, tls=True, tlsCAFile=ca, tlsAllowInvalidCertificates=False)

db = client["smart_shopper_db"]
collection = db["common_info"]

# Data Ingestion: Extract, Transform, and Load (ETL) local CSV dataset
try:
    df_movies = pd.read_csv('data/movies.csv', encoding='utf-8')
    # Preprocessing: Normalize column headers to lowercase and strip whitespace for schema consistency
    df_movies.columns = [c.lower().strip() for c in df_movies.columns]
    print("Dataset ingested. Features:", df_movies.columns.tolist())
except Exception as e:
    # Exception handling: Instantiate empty DataFrame to maintain pipeline fault tolerance
    print(f"Error during data ingestion: {e}")
    df_movies = pd.DataFrame()

def get_common_info(user_query):
    try:
        # Information Retrieval: Execute full-text search against the knowledge base
        result = collection.find({"$text": {"$search": user_query}}).limit(1)
        doc = next(result, None)
        return doc['answer'] if doc else "Maaf, informasi tersebut belum tersedia di database."
    except Exception as e:
        # Monitoring: Log runtime exceptions within the retrieval pipeline
        print(f"Log Error: {e}")
        return "Sistem sedang sibuk."

def get_movie_recommendations(user_query):
    # Data Validation: Ensure dataset is populated before initiating inference
    if df_movies.empty:
        return "Database film tidak tersedia."
        
    # Schema Validation: Verify required feature presence for the recommendation logic
    if 'title' not in df_movies.columns or 'genres' not in df_movies.columns:
        return f"Error: Required features ('title' or 'genres') not found. Available features: {df_movies.columns.tolist()}"

    # Preprocessing: Normalize query string for case-insensitive matching
    q = user_query.lower()
    
    # Vectorized Filtering: Generate boolean mask for similarity search across title and genre dimensions
    mask = (df_movies['title'].astype(str).str.lower().str.contains(q, na=False)) | \
           (df_movies['genres'].astype(str).str.lower().str.contains(q, na=False))
    
    matches = df_movies[mask]
    
    # Inference result: Return top-k records (k=5) based on filtering criteria
    if not matches.empty:
        result = matches.head(5)[['title', 'genres']].to_string(index=False)
        return f"Berikut film yang relevan dengan '{user_query}':\n\n{result}"
    else:
        # Fallback logic: Handle query-data intersection failures
        return f"Film/Genre '{user_query}' tidak ditemukan."