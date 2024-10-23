!pip install pandas

# Importing the necessary libraries
import pandas as pd
import numpy as np

# Set random seed for reproducibility (to ensure that if you run the code with the data, you get the same results every time)
# This ensures that the random numbers generated are the same each time the code is run

np.random.seed(42)

# Number of rows in the dataset
n = 1000

# Simulating the dataset
data = {
    'loan_id': np.arange(1, n+1), # Unique loan ID for each row
    'loan_amount': np.random.randint(5000, 40000, size=n), # Random loan amounts between $5,000 and $40,000
    'term': np.random.choice(['36 months', '60 months'], size=n), # Random loan term: 36 or 60 months
    'interest_rate': np.round(np.random.uniform(5.0, 25.0, size=n), 2), # Random interest rates between 5% and 25%
    'installment': np.round(np.random.uniform(150, 1000, size=n), 2), # Random monthly installment amounts between $150 and $1000
    'loan_grade': np.random.choice(['A', 'B', 'C', 'D', 'E'], size=n), # Random loan grades from A to E
    'annual_income': np.random.randint(30000, 150000, size=n), # Random annual incomes between $30,000 and $150,000
    'employment_length': np.random.choice(['<1 year', '1-3 years', '4-6 years', '7-9 years', '10+ years'], size=n), # Random employment length
    'home_ownership': np.random.choice(['RENT', 'MORTGAGE', 'OWN'], size=n), # Random home ownership status
    'debt_to_income_ratio': np.round(np.random.uniform(10.0, 40.0, size=n), 2),# Random debt-to-income ratio between 10% and 40%
    'credit_score': np.random.randint(600, 850, size=n), # Random FICO credit scores between 600 and 850
    'loan_status': np.random.choice(['Fully Paid', 'Defaulted', 'Charged Off'], size=n, p=[0.7, 0.2, 0.1]), # Loan status with specified probabilities
    'default_probability': np.round(np.random.uniform(0, 1, size=n), 2), # Random probability of default between 0 and 1
    'delinquencies_last_2yrs': np.random.randint(0, 5, size=n), # Random number of delinquencies in the past 2 years
    'revolving_credit_balance': np.random.randint(1000, 50000, size=n), # Random revolving credit balances between $1,000 and $50,000
    'total_credit_limit': np.random.randint(5000, 100000, size=n) # Random total credit limit between $5,000 and $100,000
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Saving it as a CSV file
df.to_csv('credit_risk_dataset.csv', index=False)

# Importing the files library from Colab to enable file downloads
from google.colab import files

# Download the CSV file
files.download('credit_risk_dataset.csv')
