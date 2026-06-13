import os
from groq import Groq
from dotenv import load_dotenv
from tools.retrieval import get_common_info, get_movie_recommendations
from tools.profile_utils import get_user_profile

# 1. Load environment dan inisialisasi client
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def route_query(user_query, chat_history):
    # 2. Update System Prompt dengan data profil user
    user_info = get_user_profile()
    system_prompt = f"Kamu adalah asisten belanja pribadi untuk {user_info}. Jawab pertanyaan dengan mempertimbangkan preferensi tersebut."
    
    # Memastikan index 0 ada untuk System Prompt
    if not chat_history:
        chat_history.append({"role": "system", "content": system_prompt})
    else:
        chat_history[0] = {"role": "system", "content": system_prompt}
    
    # 3. Append user input ke chat_history
    chat_history.append({"role": "user", "content": user_query})
    
    # 4. Routing Logic
    faq_keywords = ["kirim", "refund", "pembayaran", "ongkir", "kembali", "batal", "uang"]
    movie_keywords = ["film", "nonton", "rekomendasi", "movie", "genre"]
    
    try:
        if any(keyword in user_query.lower() for keyword in faq_keywords):
            response = get_common_info(user_query)
        
        elif any(keyword in user_query.lower() for keyword in movie_keywords):
            response = get_movie_recommendations(user_query)
            
        else:
            # Fallback ke Groq LLM 
            chat_completion = client.chat.completions.create(
                messages=chat_history,
                model="llama-3.3-70b-versatile", 
            )
            response = chat_completion.choices[0].message.content
            
        # Update state dengan answer asisten
        chat_history.append({"role": "assistant", "content": response})
        return response
        
    except Exception as e:
        return f"Maaf, terjadi kendala teknis: {e}"