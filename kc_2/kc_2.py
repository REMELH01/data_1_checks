import pandas as pd 
import seaborn as sns

df = pd.read_csv(r'C:\Users\rmelh\OneDrive\Documents\data_1_check\kc_2\assets\National_Universities_Rankings.csv')

sns.scatterplot(x=df['rank'],
                y=df['tuition_and_fees'])