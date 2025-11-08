import streamlit as st
import re
import math
from datetime import datetime

def evaluate_password(password):
    score = 0
    evaluation = {
        "Length": 0,
        "Complexity": 0,
        "Unpredictability": 0,
        "Entropy": 0,
        "Uniqueness": 0
    }

    if len(password) >= 12:
        evaluation["Length"] = 1
        score += 1

    complexity_criteria = [
        r'[A-Z]',
        r'[a-z]',
        r'[0-9]',
        r'[^a-zA-Z0-9]'
    ]
    complexity_count = sum(bool(re.search(criteria, password)) for criteria in complexity_criteria)
    if complexity_count >= 3:
        evaluation["Complexity"] = 1
        score += 1

    common_patterns = [
        r'(.)\1{2,}',
        r'(0123456789|9876543210|abcdefghijklmnopqrstuvwxyz|ABCDEFGHIJKLMNOPQRSTUVWXYZ)',
        r'(qwerty|asdfgh|zxcvbn|password|admin|welcome)'
    ]
    if not any(re.search(pattern, password) for pattern in common_patterns):
        evaluation["Unpredictability"] = 1
        score += 1

    pool_size = 0
    if re.search(r'[a-z]', password): pool_size += 26
    if re.search(r'[A-Z]', password): pool_size += 26
    if re.search(r'[0-9]', password): pool_size += 10
    if re.search(r'[^a-zA-Z0-9]', password): pool_size += 32

    entropy = len(password) * math.log2(pool_size or 1)
    if entropy >= 60:
        evaluation["Entropy"] = 1
        score += 1

    if evaluation["Unpredictability"]:
        evaluation["Uniqueness"] = 1
        score += 1

    evaluation["Score"] = f"{score}/5"
    return evaluation


def generate_game_code(first_name, last_name, dob, phone, pet_name, clues):
    try:
        code = (
            clues[0][:2].capitalize() +
            first_name[:2].capitalize() +
            clues[1][:2].lower() +
            dob.strftime("%d%Y") +
            clues[2][:2].capitalize() +
            phone[-2:] +
            clues[3][:1].upper() +
            pet_name.capitalize()[:2] +
            clues[4][-1] + "@#"
        )
        return code
    except Exception:
        return "Invalid input! Please fill all details correctly."


st.set_page_config(page_title="Password Strength Assessment Tool", page_icon="🔐")
st.title("🔐 Password Strength Assessment Tool")
st.subheader("Build and Test Your Password Strength with AI-Powered Evaluation")

st.divider()
st.header("🧩 Enter Your Personal Details")

first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
dob = st.date_input("Date of Birth", datetime.now())
phone = st.text_input("Phone Number")
pet_name = st.text_input("Pet Name")

if st.button("Generate & Test Password"):
    clues = ["Star", "Moon", "Sun", "Cloud", "Rain"]
    game_code = generate_game_code(first_name, last_name, dob, phone, pet_name, clues)

    st.success(f"✅ Generated Password: {game_code}")

    evaluation = evaluate_password(game_code)
    st.write("### 🧠 Password Strength Evaluation:")
    for factor, result in evaluation.items():
        emoji = "✔️" if result else "❌"
        st.write(f"{emoji} {factor}: {result if isinstance(result, str) else ('Pass' if result else 'Fail')}")