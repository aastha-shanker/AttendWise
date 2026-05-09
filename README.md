# 🎓 AttendWise

## 🌐 Live Demo

🔗 **Try AttendWise Live:** [Open App](YOUR_STREAMLIT_LINK)

---

# 📌 About The Project

AttendWise is a **Machine Learning powered web application** that predicts whether a student is eligible to sit for exams based on subject-wise attendance.

The project uses **Logistic Regression** along with a **weighted aggregate attendance system** to analyze attendance patterns and generate eligibility predictions with probability scores.

---

# 🚀 Features

- 📊 Subject-wise attendance input
- ⚖ Weighted aggregate attendance calculation
- 🤖 Logistic Regression based prediction
- 📈 Eligibility probability analysis
- 🎚 Interactive slider-based UI
- ⚠ Risk status detection
- 💡 Attendance improvement suggestions
- 🌐 Streamlit web deployment

---

# 🧠 Machine Learning Workflow

This project follows a complete ML pipeline:

1. Dataset creation
2. Feature engineering
3. Data preprocessing
4. Train-test split
5. Logistic Regression model training
6. Model evaluation
7. Pickle model serialization
8. Streamlit deployment

---

# 📚 Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Streamlit**
- **Matplotlib**

---

# ⚙ How It Works

Each subject is assigned credits (weights).

The system calculates weighted aggregate attendance using:

Aggregate = Σ(Attendance × Credits) / Σ(Credits)
The trained Logistic Regression model then predicts:

✅ Eligible for Exams
❌ Debarred from Exams

along with prediction probability.

---
# 📂 Project Structure
AttendWise/
│
├── app.py
├── train_model.py
├── students_attendance.csv
├── attendance_model.pkl
├── requirements.txt
└── README.md

---

# 📸 Future Improvements

📊 Analytics dashboard
📁 Multi-student CSV upload
🤖 AI chatbot integration
📈 Advanced visualization
🌙 Custom UI themes
☁ Cloud database integration
--- 

# 🎯 Learning Outcomes

This project helped in understanding:

Logistic Regression
Classification problems
Feature engineering
Model deployment
Streamlit UI development
End-to-end ML workflow
---
# 👩‍💻 Author

Aastha Shanker