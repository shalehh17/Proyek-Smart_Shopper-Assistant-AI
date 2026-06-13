===========================================================


PROYEK: PERSONALIZED SMART-SHOPPER ASSISTANT


===========================================================

DESKRIPSI PROYEK
----------------
Personalized Smart-Shopper Assistant adalah asisten belanja cerdas berbasis AI 
yang dirancang untuk memberikan rekomendasi belanja yang dipersonalisasi. 
Sistem ini mengintegrasikan data profil pengguna (JSON), basis pengetahuan FAQ 
(MongoDB), dan data film (CSV) untuk memberikan respons yang relevan, 
terstruktur, dan personal.

FITUR UTAMA
-----------
1. Personalization Engine: Memberikan respons berdasarkan profil unik pengguna.
2. Intelligent Retrieval: Menggunakan MongoDB Full-Text Search untuk menjawab FAQ.
3. Movie Recommendation: Sistem filter cerdas untuk mencari film berdasarkan judul atau genre.
4. AI-Powered: Terintegrasi dengan model bahasa besar (Groq API) untuk percakapan natural.

WORKFLOW (ALUR KERJA)
---------------------
1. User Query: Pengguna memasukkan input teks.
2. Intent Classification: Sistem mengklasifikasikan query apakah masuk ke kategori FAQ, Rekomendasi Film, atau Chat Umum.
3. Data Retrieval:
   - Jika FAQ: Query dikirim ke MongoDB `smart_shopper_db`.
   - Jika Rekomendasi Film: Sistem memproses `movies.csv` menggunakan Pandas.
4. LLM Generation: Jika tidak masuk kedua kategori di atas, query diteruskan ke model Groq (Llama-3).
5. Response: Asisten memberikan jawaban akhir kepada pengguna.

STRUKTUR FOLDER
---------------
/data           : Berisi file dataset (movies.csv, ratings.csv, dll) dan user_profile.json.
/src            : Berisi file utama agen (agent.py) untuk logika AI.
/tools          : Berisi fungsi-fungsi pendukung (retrieval.py, profile_utils.py).
app.py          : Antarmuka web menggunakan Streamlit.
main.py         : Entry point untuk menjalankan asisten di terminal.
setup_db.py     : Script untuk sinkronisasi data ke MongoDB.
.env            : File konfigurasi rahasia (API Key & Mongo URI).

PANDUAN INSTALASI
-----------------
1. Clone repositori: git clone https://github.com/shalehh17/smart-shopper-assistant.git
2. Instal dependensi: pip install -r requirements.txt
3. Konfigurasi .env: Masukkan GROQ_API_KEY dan MONGO_URI.
4. Setup Database: Jalankan `python setup_db.py`.
5. Jalankan Aplikasi: `streamlit run app.py`

===========================================================
