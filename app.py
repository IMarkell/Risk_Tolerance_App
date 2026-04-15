import streamlit as st

# Title of the app
st.title('Risk Tolerance Questionnaire')

# Questions and their choices
questions = [
    "How comfortable are you with the possibility of losing money in the short term if it means potentially earning more in the long term?",
    "How would you feel if your investment dropped 20% in a single year?",
    "How would you feel if you had a 50/50 chance of doubling your money or losing it all?",
    "How comfortable are you making financial decisions when the outcome is uncertain?",
    "How comfortable are you with investing in assets that may take several years to recover from downturns?"
]

choices = [
    "1 - Not comfortable at all",
    "2 - Slightly uncomfortable",
    "3 - Neutral",
    "4 - Slightly comfortable",
    "5 - Very comfortable"
]

# Initialize total score
total_score = 0

# Ask each question to the user
for question in questions:
    response = st.radio(question, choices)
    total_score += int(response.split()[0])  # Extract the numerical score from the choice

# Display the total score
st.write(f'\nTotal score: {total_score}')

# Categorize user based on score
if total_score <= 12:
    st.write('You have a Low Risk Tolerance.')
elif total_score <= 19:
    st.write('You have a Medium Risk Tolerance.')
else:
    st.write('You have a High Risk Tolerance.')
