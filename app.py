import streamlit as st

# Title of the app
st.title('Risk Tolerance: What you should invest in?')

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
    st.write('You have a Low Risk Tolerance.'
            'Goal: Capital preservation, stability, minimal volatility
Suggested Allocation:

60–80% Bonds / Fixed Income

10–25% Large‑Cap, Low‑Volatility Stocks

0–10% International Developed Markets

0–5% Alternatives (REITs, TIPS)

Why this fits low‑risk clients:

Bonds reduce portfolio volatility and provide predictable income.

Large‑cap stocks (e.g., S&P 500 companies) offer stability with lower drawdowns.

Minimal exposure to international or small‑cap equities avoids unnecessary volatility.')
elif total_score <= 19:
    st.write('You have a Medium Risk Tolerance.'
    Goal: Balanced growth and stability
Suggested Allocation:

40–60% Stocks (U.S. + International)

30–50% Bonds / Fixed Income

5–10% Alternatives (REITs, commodities, TIPS)

Why this fits medium‑risk clients:

Balanced portfolios smooth volatility while still capturing equity‑driven growth.

International exposure improves diversification and reduces correlation.

Bonds stabilize returns during market downturns.)
else:
    st.write('You have a High Risk Tolerance.'
    Goal: Maximum long‑term growth, accepts volatility
Suggested Allocation:

70–90% Stocks (U.S., International, Emerging Markets)

5–20% Bonds (mainly short‑term or high‑yield)

5–10% Alternatives (REITs, commodities, thematic ETFs)

Why this fits high‑risk clients:

High equity exposure maximizes long‑term return potential.

Emerging markets and small‑cap stocks add growth but increase volatility.

Minimal bond exposure keeps the portfolio aggressive and growth‑oriented.)
