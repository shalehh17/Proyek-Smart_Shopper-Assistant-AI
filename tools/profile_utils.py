import json

def get_user_profile():
    try:
        with open('data/user_profile.json', 'r') as file:
            profile = json.load(file)
            # ubah profil menjadi string untuk disuntikkan ke System Prompt
            return f"Nama: {profile['name']}. Preferensi: {', '.join(profile['preferences'])}. Gaya belanja: {profile['shopping_style']}."
    except Exception as e:
        return "Pengguna umum."
