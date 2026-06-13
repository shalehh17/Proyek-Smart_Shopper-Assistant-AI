from src.agent import route_query

def main():
    # Inisialisasi State (chat_history kosong di awal, 
    # System Prompt akan disuntikkan secara dinamis di agent.py)
    chat_history = [{"role": "system", "content": "Initializing..."}]
    
    print("--- Smart Shopper Assistant v1.0 [Personalized] ---")
    print("Agent siap. Ketik 'exit' untuk mengakhiri sesi.")
    
    while True:
        user_input = input("\nAnda: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Sampai jumpa kembali!")
            break
        
        # Invoke agent router
        response = route_query(user_input, chat_history)
        print(f"Agent: {response}")

if __name__ == "__main__":
    main()