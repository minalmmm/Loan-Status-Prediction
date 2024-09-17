import streamlit as st
import pandas as pd
import numpy as np

# Streamlit App
st.title('Loan Status Prediction Dashboard')

# Input Fields
st.sidebar.header('User Input Features')

def user_input_features():
    gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
    married = st.sidebar.selectbox('Married', ['No', 'Yes'])
    education = st.sidebar.selectbox('Education', ['Graduate', 'Not Graduate'])
    self_employed = st.sidebar.selectbox('Self Employed', ['No', 'Yes'])
    applicant_income = st.sidebar.slider('Applicant Income', 0, 100000, 5000)
    loan_amount = st.sidebar.slider('Loan Amount', 0, 600000, 200000)
    loan_amount_term = st.sidebar.slider('Loan Amount Term (in months)', 12, 480, 360)
    credit_history = st.sidebar.selectbox('Credit History', [0, 1])
    property_area = st.sidebar.selectbox('Property Area', ['Rural', 'Semiurban', 'Urban'])
    
    data = {
        'Gender': gender,
        'Married': married,
        'Education': education,
        'Self_Employed': self_employed,
        'ApplicantIncome': applicant_income,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_amount_term,
        'Credit_History': credit_history,
        'Property_Area': property_area
    }
    
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Display user inputs
st.write('### User Input Features')
st.write(df)

# Simulate prediction with a simple rule-based approach
def predict_loan_status(df):
    # Dummy prediction logic: If credit history is 1 and income is above a threshold, approve the loan
    if df['Credit_History'][0] == 1 and df['ApplicantIncome'][0] > 30000:
        return 1  # Loan Approved
    else:
        return 0  # Loan Rejected

if st.button('Predict'):
    # Simulate prediction
    prediction = predict_loan_status(df)
    
    # Display prediction
    if prediction == 0:
        st.write('### The loan is likely to be rejected.')
    else:
        st.write('### The loan is likely to be approved.')

# For additional details and customizations
st.write("""
### Details:
This dashboard uses a simple rule-based approach to predict loan approval based on user input features. Adjust the input values in the sidebar and click "Predict" to see the result.
""")

