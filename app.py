import streamlit as st
import pandas as pd
import pickle

# load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# subject credits
credits = {
    "Maths": 4,
    "DS": 3,
    "TOC": 3,
    "DBMS": 2,
    "Java": 2
}

# title
st.set_page_config(
    page_title="AttendWise",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AttendWise")

st.markdown("""
### Smart Exam Eligibility Predictor

Predict whether a student is eligible for exams
based on weighted attendance analysis.
""")

st.sidebar.header("📘 About")

st.sidebar.write("""
AttendWise uses Logistic Regression to predict
student exam eligibility based on attendance data.
""")

st.sidebar.write("Developed using:")
st.sidebar.write("- Python")
st.sidebar.write("- Scikit-learn")
st.sidebar.write("- Streamlit")

st.write("Enter student attendance below:")

# user inputs
col1, col2 = st.columns(2)

with col1:
    maths = st.slider(
        "Maths Attendance",
        0, 100, 75
    )

    ds = st.slider(
        "DS Attendance",
        0, 100, 75
    )

    toc = st.slider(
        "TOC Attendance",
        0, 100, 75
    )

with col2:
    dbms = st.slider(
        "DBMS Attendance",
        0, 100, 75
    )

    java = st.slider(
        "Java Attendance",
        0, 100, 75
    )

# button
if st.button("Predict Eligibility"):

    # calculate weighted aggregate
    aggregate = (
        maths * credits['Maths'] +
        ds * credits['DS'] +
        toc * credits['TOC'] +
        dbms * credits['DBMS'] +
        java * credits['Java']
    ) / sum(credits.values())

    # create dataframe
    sample = pd.DataFrame({
        'Maths': [maths],
        'DS': [ds],
        'TOC': [toc],
        'DBMS': [dbms],
        'Java': [java],
        'aggregate': [aggregate]
    })

    # prediction
    prediction = model.predict(sample)

    # probability
    probability = model.predict_proba(sample)
    pass_prob = probability[0][1] * 100
    if pass_prob >= 90:
      risk = "🟢 SAFE"

    elif pass_prob >= 70:
      risk = "🟡 WARNING"

    else:
      risk = "🔴 HIGH RISK"
      
    subjects = {
    "Maths": maths,
    "DS": ds,
    "TOC": toc,
    "DBMS": dbms,
    "Java": java
}
    

    low_subjects = []

    for subject, attendance in subjects.items():
      if attendance < 75:
        low_subjects.append(subject)

    # results
    st.metric(
    label="Aggregate Attendance",
    value=f"{aggregate:.2f}%"
)
    
    if prediction[0] == 1:
        st.success("✅ Student is ELIGIBLE for exams")
        
    
    else:
        st.error("❌ Student is DEBARRED from exams")
    
    st.metric(
    "Risk Status",
    risk
)
    if low_subjects:

      st.warning(
        f"⚠ Improve attendance in: {', '.join(low_subjects)}"
    )

    else:
      st.success("🎉 Attendance looks good in all subjects!")
    