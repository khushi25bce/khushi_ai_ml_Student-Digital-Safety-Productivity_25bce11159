import streamlit as st
import numpy as np
from sklearn.linear_model import LogisticRegression

st.title("🎓 Student Performance Predictor")

# Dummy training data
X = np.array([
    [2, 60, 5, 50],
    [5, 80, 6, 70],
    [1, 40, 4, 30],
    [6, 90, 7, 85],
    [3, 70, 5, 60]
])
y = np.array([0, 1, 0, 1, 1])  # 0 = Fail, 1 = Pass

model = LogisticRegression()
model.fit(X, y)

st.header("Enter Student Details")

study = st.slider("Study Hours", 0, 10)
attendance = st.slider("Attendance (%)", 0, 100)
sleep = st.slider("Sleep Hours", 0, 10)
marks = st.slider("Previous Marks", 0, 100)

if st.button("Predict"):
    prediction = model.predict([[study, attendance, sleep, marks]])
    
    if prediction[0] == 1:
        st.success("✅ Student will PASS")
    else:
        st.error("❌ Student may FAIL")