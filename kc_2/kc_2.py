import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt

dataframe = pd.read_csv('National_Universities_Rankings.csv')

Rank = dataframe('Rank')
Tuition_and_Fees = dataframe('tuition_and_fees')

plt.plot(Rank, Tuition_and_Fees, marker="^")
plt.show()