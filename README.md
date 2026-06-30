# 🛒 Personalized Smart-Shopper Assistant

## 📝 Deskripsi Proyek
**Personalized Smart-Shopper Assistant** adalah asisten belanja cerdas berbasis AI yang dirancang untuk memberikan rekomendasi belanja yang dipersonalisasi. Sistem ini mengintegrasikan data profil pengguna (JSON), basis pengetahuan FAQ (MongoDB), dan data film (CSV) untuk memberikan respons yang relevan, terstruktur, dan personal.

---

## ✨ Fitur Utama
* **Personalization Engine:** Memberikan respons adaptif berdasarkan profil unik pengguna.
* **Intelligent Retrieval:** Menggunakan *MongoDB Full-Text Search* untuk menjawab FAQ secara cepat dan akurat.
* **Movie Recommendation:** Sistem filter cerdas menggunakan Pandas untuk mencari film berdasarkan judul atau genre.
* **AI-Powered:** Terintegrasi dengan *Large Language Model* (Groq API) untuk menghasilkan percakapan yang natural dan kontekstual.

---

## 🔄 Alur Kerja (Workflow)

[ User Query ] ──> [ Intent Classification ]
│
┌────────────────────┼────────────────────┐
▼                    ▼                    ▼
[ Kategori FAQ ]   [ Rekomendasi Film ]   [ Chat Umum ]
│                    │                    │
▼                    ▼                    ▼
(MongoDB Search)    (Pandas - CSV)        (Groq LLM)
│                    │                    │
└────────────────────┼────────────────────┘
▼
[ Response Akhir ]


1. **User Query:** Pengguna memasukkan input teks melalui antarmuka.
2. **Intent Classification:** Sistem secara otomatis mengklasifikasikan *query* ke dalam kategori FAQ, Rekomendasi Film, atau Chat Umum.
3. **Data Retrieval:**
   * **Jika FAQ:** *Query* dikirim ke MongoDB di dalam database `smart_shopper_db`.
   * **Jika Rekomendasi Film:** Sistem memproses data pada file `movies.csv` menggunakan library Pandas.
4. **LLM Generation:** Jika *query* masuk ke kategori Chat Umum, proses akan diteruskan ke model bahasa Groq (Llama-3).
5. **Response:** Asisten menyusun dan memberikan jawaban akhir yang dipersonalisasi kepada pengguna.

---

## 📁 Struktur Folder
```text
.
├── data/
│   ├── movies.csv          # Dataset film untuk sistem rekomendasi
│   ├── ratings.csv         # Dataset rating film
│   └── user_profile.json   # Data profil unik pengguna
├── src/
│   └── agent.py            # Logika utama AI agen
├── tools/
│   ├── profile_utils.py    # Fungsi pendukung manajemen profil
│   └── retrieval.py        # Fungsi pendukung pencarian data
├── .env                    # File konfigurasi rahasia (API Key & URI)
├── app.py                  # Antarmuka web berbasis Streamlit
├── main.py                 # Entry point untuk menjalankan asisten via terminal



🚀 Panduan Instalasi
Ikuti langkah-langkah berikut untuk menjalankan proyek ini di lingkungan lokal:

1. Clone Repositori
Bash
git clone [https://github.com/shalehh17/smart-shopper-assistant.git](https://github.com/shalehh17/smart-shopper-assistant.git)
cd smart-shopper-assistant
2. Instal Dependensi
Pastikan Anda sudah menginstal Python, kemudian jalankan perintah berikut:

Bash
pip install -r requirements.txt
3. Konfigurasi Environment Variables
Buat sebuah file bernama .env di direktori utama proyek, lalu masukkan konfigurasi berikut:

Cuplikan kode
GROQ_API_KEY=your_groq_api_key_here
MONGO_URI=your_mongodb_uri_here
4. Setup Database
Jalankan script berikut untuk melakukan sinkronisasi data awal ke MongoDB:

Bash
python setup_db.py
5. Jalankan Aplikasi
Anda dapat memilih untuk menjalankan aplikasi melalui antarmuka web (Streamlit) atau terminal:

Menjalankan Web App (Streamlit):

Bash
streamlit run app.py
Menjalankan via Terminal:

Bash
python main.py



├── requirements.txt        # Daftar dependensi library Python
└── setup_db.py             # Script sinkronisasi data ke MongoDB
