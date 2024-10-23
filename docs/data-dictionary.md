# Data Dictionary for Credit Risk Scoring Model

## Overview
This document describes the structure of a synthetic dataset designed for a **Credit Risk Scoring Model**. The dataset simulates borrower profiles, loan data, and outcomes, incorporating key financial metrics such as **FICO scores** to predict loan default risk.

## 1. Loan Information

| **Column Name**  | **Data Type** | **Description**                                                                                  | **Example Values**      |
|------------------|---------------|--------------------------------------------------------------------------------------------------|-------------------------|
| `loan_id`        | Integer       | Unique identifier for each loan.                                                                  | 1, 2, 3, ...            |
| `loan_amount`    | Integer       | Total loan amount borrowed by the individual, in USD.                                         | 5000, 15000, 40000       |
| `term`           | String        | Loan repayment term, indicating the duration over which the loan is to be repaid.              | "36 months", "60 months" |
| `interest_rate`  | Float         | Annual interest rate charged on the loan, as a percentage.                                       | 5.50, 15.75, 24.99       |
| `installment`    | Float         | Monthly payment amount due, including both interest and principal.                                | 150.45, 600.75, 1000.20  |
| `loan_grade`     | String        | Loan risk grade assigned based on borrower profile, typically ranging from "A" (best) to "E" (worst). | "A", "B", "C", "D", "E" |

## 2. Borrower Information

| **Column Name**      | **Data Type** | **Description**                                                                                        | **Example Values**      |
|----------------------|---------------|--------------------------------------------------------------------------------------------------------|-------------------------|
| `annual_income`       | Integer       | Borrower’s self-reported annual income in USD.                                                           | 30000, 75000, 120000     |
| `employment_length`   | String        | Number of years the borrower has been employed, categorized into ranges.                                 | "<1 year", "4-6 years", "10+ years" |
| `home_ownership`      | String        | Borrower’s homeownership status, a key indicator of financial stability.                                 | "RENT", "MORTGAGE", "OWN" |
| `debt_to_income_ratio`| Float         | Ratio of total monthly debt payments to gross monthly income, expressed as a percentage.                 | 15.25, 30.50, 40.00      |
| `credit_score`        | Integer       | Borrower's **FICO score**, which reflects their overall creditworthiness. Ranges from 300 to 850.        | 600, 720, 850            |

## 3. Loan Outcome

| **Column Name**    | **Data Type** | **Description**                                                                                           | **Example Values**          |
|--------------------|---------------|-----------------------------------------------------------------------------------------------------------|-----------------------------|
| `loan_status`      | String        | Indicates the current status of the loan (e.g., repaid, defaulted, or charged off).                        | "Fully Paid", "Defaulted", "Charged Off" |
| `default_probability`| Float       | Estimated probability that the borrower will default on the loan, often modeled using statistical methods. | 0.05, 0.35, 0.95            |

## 4. Credit History

| **Column Name**              | **Data Type** | **Description**                                                                                           | **Example Values**      |
|------------------------------|---------------|-----------------------------------------------------------------------------------------------------------|-------------------------|
| `delinquencies_last_2yrs`     | Integer       | Number of delinquencies (late payments or defaults) the borrower has had in the past two years.             | 0, 2, 4                 |
| `revolving_credit_balance`    | Integer       | Total revolving credit balance (such as credit card debt) that the borrower currently holds, in USD.         | 1500, 10000, 30000       |
| `total_credit_limit`          | Integer       | Total amount of revolving credit available to the borrower across all credit accounts, in USD.              | 5000, 25000, 100000      |

## Detailed Description of Key Features

1. **FICO Score (`credit_score`)**:  
   The FICO score is a credit scoring model used by lenders to evaluate credit risk. Scores range from 300 to 850, where higher scores indicate better creditworthiness and lower risk of default.  
   - **300-579**: Poor  
   - **580-669**: Fair  
   - **670-739**: Good  
   - **740-799**: Very Good  
   - **800-850**: Excellent  

2. **Debt-to-Income Ratio (`debt_to_income_ratio`)**:  
   This ratio compares a borrower’s monthly debt payments to their gross monthly income. It is a key metric used to assess a borrower’s capacity to repay new debts. A higher ratio suggests higher financial strain, increasing the risk of default.

3. **Loan Grades (`loan_grade`)**:  
   Loan grades reflect the risk profile of the borrower and are used by lending institutions to determine loan pricing.  
   - **A**: Lowest risk  
   - **B**: Low risk  
   - **C**: Moderate risk  
   - **D**: Higher risk  
   - **E**: Highest risk  

4. **Loan Status (`loan_status`)**:  
   This categorical field indicates the outcome of the loan:
   - **Fully Paid**: Loan was successfully repaid.
   - **Defaulted**: Borrower failed to meet repayment obligations.
   - **Charged Off**: The lender has deemed the loan uncollectible and written it off as a loss.

## Notes
- **Data Quality**: The dataset should be cleaned before analysis. For example, missing or erroneous values in income, credit score, or loan status should be handled appropriately.
- **Predictive Modeling**: The fields in this dataset, especially `credit_score`, `loan_grade`, `debt_to_income_ratio`, and `loan_status`, can be used to predict the likelihood of loan default, which is critical for the development of the credit risk scoring model.
