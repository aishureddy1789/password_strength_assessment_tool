# 🔐 Password Strength Assessment Tool

A **Streamlit-based web application** that evaluates password strength using multiple security metrics and generates a personalized password using user inputs and predefined clues.  

---

## 🚀 Features

- **AI-powered password evaluation**  
  Evaluates passwords based on:
  - Length  
  - Complexity (uppercase, lowercase, digits, symbols)  
  - Unpredictability (detects common patterns)  
  - Entropy (mathematical randomness)  
  - Uniqueness  

- **Smart password generation**  
  Dynamically creates a unique password using:
  - First name  
  - Last name  
  - Date of birth  
  - Phone number  
  - Pet name  
  - A list of hint words (“clues”)

- **Interactive Streamlit interface**  
  User-friendly web UI to test and visualize password strength.

---

## 🧠 How It Works

1. Enter your personal details (first name, last name, date of birth, phone number, and pet name).  
2. Click **“Generate & Test Password”**.  
3. The app will:
   - Generate a password using the given inputs and clue words.  
   - Evaluate it across five key security metrics.  
   - Display a detailed report on its strength.

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/password-strength-assessment.git
cd password-strength-assessment
```


2. Install dependencies
```bash
pip install streamlit
```

3. Run the app
```bash
streamlit run main.py
```

---
## 📊 Evaluation Logic

| Metric               | Description                                      | Pass Criteria              |
| :------------------- | :----------------------------------------------- | :------------------------- |
| **Length**           | Password length check                            | ≥ 12 characters            |
| **Complexity**       | Checks presence of upper, lower, digits, symbols | ≥ 3 types present          |
| **Unpredictability** | Avoids common patterns or sequences              | No repeated/common strings |
| **Entropy**          | Information-theoretic randomness                 | ≥ 60 bits                  |
| **Uniqueness**       | Derived from unpredictability                    | True if unpredictable      |
---
## 🧩 Example

**Input:**

* First Name: `Alice`
* Last Name: `Smith`
* DOB: `1998-04-22`
* Phone: `9876543210`
* Pet Name: `Milo`

**Generated Password:**

```
StAlmo221998Su10CMi#@ 
```

**Evaluation Result:**

```
✔ Length: Pass
✔ Complexity: Pass
✔ Unpredictability: Pass
✔ Entropy: Pass
✔ Uniqueness: Pass
Score: 5/5
```

---