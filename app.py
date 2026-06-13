import streamlit as st
from src.agent import route_query

# 1. Page Configuration: Define UI metadata and layout parameters
st.set_page_config(page_title="Smart Shopper AI", page_icon="🛍️", layout="centered")

# 2. UI Styling: Inject custom CSS for enhanced visualization and theme consistency
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .stChatMessage { border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Configuration: Define auxiliary controls and user instructions
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3081/3081559.png", width=100)
    st.title("🛍️ Smart Shopper")
    st.info("Asisten pribadi untuk belanja, film, dan bantuan FAQ.")
    
    st.divider()
    st.subheader("💡 Tips Cepat:")
    st.write("• 'Rekomendasi film Action'")
    st.write("• 'Bagaimana cara refund?'")
    st.write("• 'Apa hobi saya?'")
    
    # State Reset: Clear session cache to purge conversation memory
    if st.button("🔄 Reset Percakapan"):
        st.session_state.messages = []
        st.rerun()

# 4. Interface Header: Define main application identity
st.title("✨ AI Personal Assistant")
st.caption("Ditenagai oleh Llama-3.3-70b & Database Pintar")

# 5. State Initialization: Instantiate persistent chat history object
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo Shalehuddin Zaki! Ada yang bisa saya bantu hari ini?"}
    ]

# 6. View Rendering: Display accumulated dialogue context from session state
for message in st.session_state.messages:
    role_icon = "👤" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=role_icon):
        st.markdown(message["content"])

# 7. Input Processing & Inference Pipeline: Handle user interaction and model routing
if prompt := st.chat_input("Tanyakan sesuatu (Contoh: Film Action, Refund, dll)..."):
    # Append input to session history for context-aware interaction
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Inference step: Execute model request with progress feedback
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Sedang memproses inferensi model..."):
            response = route_query(prompt, st.session_state.messages)
            st.markdown(response)
    
    # State update: Persist model response into history object
    st.session_state.messages.append({"role": "assistant", "content": response})
