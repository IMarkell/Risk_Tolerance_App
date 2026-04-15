import streamlit as st

# Initialize session state for user responses
if 'responses' not in st.session_state:
    st.session_state.responses = ['', '', '', '', '']

# Function to display each question and get user response
def display_question(question, index):
    st.session_state.responses[index] = st.radio(question, ['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'], index=st.session_state.responses[index] if st.session_state.responses[index] != '' else 2)

# List of assessment questions
questions = [
    "1. I prefer investments that have high growth potential, even if they come with high risks.",
    "2. I am comfortable with the possibility of losing money in order to achieve greater returns.",
    "3. My investment horizon is long-term, aiming for growth over several years.",
    "4. I am knowledgeable about the financial markets and investment strategies.",
    "5. I have a financial cushion that can absorb short-term losses without affecting my lifestyle."
]

# Display all questions
st.title('Risk Tolerance Assessment')
for i, question in enumerate(questions):
    display_question(question, i)

# Calculate total score based on user responses
scores = [4, 3, 2, 1, 0]  # Scoring for Strongly Agree to Strongly Disagree
total_score = sum([scores[int(response)] for response in st.session_state.responses])

# Define risk profiles
risk_profiles = {
    'Low': {
        'goal': 'Preserve capital and achieve a modest return.',
        'allocation': '20% Stocks, 80% Bonds',
        'rationale': 'Low-risk tolerance, focusing on capital preservation.',
        'summary': 'Invest primarily in bonds and stable assets.'
    },
    'Medium': {
        'goal': 'Achieve balanced growth while managing risk.',
        'allocation': '50% Stocks, 50% Bonds',
        'rationale': 'Moderate risk tolerance, seeks growth with some safety.',
        'summary': 'Mix of stocks and bonds for balanced portfolio.'
    },
    'High': {
        'goal': 'Maximize growth potential and returns.',
        'allocation': '80% Stocks, 20% Bonds',
        'rationale': 'High-risk tolerance, accepting volatility for higher returns.',
        'summary': 'Aggressive approach with a focus on stock investments.'
    }
}

# Determine risk profile based on total score
if total_score <= 10:
    profile = 'Low'
elif total_score <= 15:
    profile = 'Medium'
else:
    profile = 'High'

# Display results
st.header(f"Your Risk Profile: {profile}")
st.write(f"**Goal:** {risk_profiles[profile]['goal']}")
st.write(f"**Recommended Asset Allocation:** {risk_profiles[profile]['allocation']}")
st.write(f"**Rationale:** {risk_profiles[profile]['rationale']}")
st.write(f"**Summary:** {risk_profiles[profile]['summary']}")
