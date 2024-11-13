
import random
import pandas as pd

# Define the number of rows
num_rows = 2000

# Helper functions to generate random data
def random_customer_id():
    return 'CUST' + str(random.randint(1000, 9999)).zfill(4)

def random_age():
    return random.randint(18, 70)

def random_account_balance():
    return round(random.uniform(1000.00, 50000.00), 2)

def random_monthly_spending():
    return round(random.uniform(500.00, 10000.00), 2)

def random_investment_portfolio_value():
    return round(random.uniform(1000.00, 100000.00), 2)

def random_risk_score():
    return random.choice(['High', 'Medium', 'Low'])

def random_sector_exposure():
    sectors = ['Technology', 'Finance', 'Healthcare', 'Energy', 'Materials', 'Consumer Goods', 'Utilities', 'Industrials', 'Real Estate']
    return ', '.join(random.sample(sectors, k=random.randint(1, 3)))

def random_high_value_transactions():
    return random.randint(0, 10)

def random_loan_amount():
    return round(random.uniform(0, 30000.00), 2)

def random_credit_score():
    return random.randint(300, 850)

def random_investment_return_rate():
    return round(random.uniform(0.00, 10.00), 2)

def random_predicted_risk():
    return random.choice(['High', 'Medium', 'Low'])

def random_suggested_product():
    products = ['Wealth Management', 'Retirement Plan', 'Credit Card', 'Pension Fund', 'Savings Account', 'Investment Account', 'Mortgage', 'Personal Loan']
    return random.choice(products)

def random_preferred_sector():
    sectors = ['Technology', 'Finance', 'Healthcare', 'Energy', 'Materials', 'Consumer Goods', 'Utilities', 'Industrials', 'Real Estate']
    return random.choice(sectors)

def random_investment_horizon():
    return random.choice(['Short-Term', 'Medium-Term', 'Long-Term'])

def random_global_event_impact():
    return random.choice(['Low', 'Moderate', 'High'])

def random_engagement_score():
    return random.randint(50, 100)

def random_profitability_score():
    return random.choice(['High', 'Medium', 'Low'])

# Generate synthetic data
data = {
    'Customer_ID': [random_customer_id() for _ in range(num_rows)],
    'Age': [random_age() for _ in range(num_rows)],
    'Account_Balance': [random_account_balance() for _ in range(num_rows)],
    'Monthly_Spending': [random_monthly_spending() for _ in range(num_rows)],
    'Investment_Portfolio_Value': [random_investment_portfolio_value() for _ in range(num_rows)],
    'Risk_Score': [random_risk_score() for _ in range(num_rows)],
    'Sector_Exposure': [random_sector_exposure() for _ in range(num_rows)],
    'High_Value_Transactions': [random_high_value_transactions() for _ in range(num_rows)],
    'Loan_Amount': [random_loan_amount() for _ in range(num_rows)],
    'Credit_Score': [random_credit_score() for _ in range(num_rows)],
    'Investment_Return_Rate': [random_investment_return_rate() for _ in range(num_rows)],
    'Predicted_Risk': [random_predicted_risk() for _ in range(num_rows)],
    'Suggested_Product': [random_suggested_product() for _ in range(num_rows)],
    'Preferred_Sector': [random_preferred_sector() for _ in range(num_rows)],
    'Investment_Horizon': [random_investment_horizon() for _ in range(num_rows)],
    'Global_Event_Impact': [random_global_event_impact() for _ in range(num_rows)],
    'Engagement_Score': [random_engagement_score() for _ in range(num_rows)],
    'Profitability_Score': [random_profitability_score() for _ in range(num_rows)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('synthetic_data.csv', index=False)

print("Synthetic data generated and saved to 'synthetic_data.csv'")
