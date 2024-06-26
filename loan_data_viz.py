# -*- coding: utf-8 -*-
"""Loan_Data_Viz.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cAoUYjSKvU-WUXorewNk-fxg8lCpk_iN
"""

import matplotlib.pyplot as plt

# Sample loan data
loan_amounts = [10000, 20000, 15000, 30000, 25000]
interest_rates = [5, 6, 4, 7, 5]
loan_terms = [12, 24, 18, 36, 30]

# Visualizing loan amounts
plt.figure(figsize=(10, 5))
plt.bar(range(len(loan_amounts)), loan_amounts, color='skyblue')
plt.xlabel('Loan')
plt.ylabel('Loan Amount ($)')
plt.title('Loan Amounts')
plt.xticks(range(len(loan_amounts)), [f'Loan {i+1}' for i in range(len(loan_amounts))])
plt.show()

# Visualizing interest rates
plt.figure(figsize=(10, 5))
plt.bar(range(len(interest_rates)), interest_rates, color='lightgreen')
plt.xlabel('Loan')
plt.ylabel('Interest Rate (%)')
plt.title('Interest Rates')
plt.xticks(range(len(interest_rates)), [f'Loan {i+1}' for i in range(len(interest_rates))])
plt.show()

# Visualizing loan terms
plt.figure(figsize=(10, 5))
plt.bar(range(len(loan_terms)), loan_terms, color='salmon')
plt.xlabel('Loan')
plt.ylabel('Loan Term (months)')
plt.title('Loan Terms')
plt.xticks(range(len(loan_terms)), [f'Loan {i+1}' for i in range(len(loan_terms))])
plt.show()