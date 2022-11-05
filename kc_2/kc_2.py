import pandas as pd 
import seaborn as sns

df = pd.read_csv(r'C:\Users\rmelh\OneDrive\Documents\data_1_check\kc_2\assets\chord_progressions.csv')

sns.scatterplot(x=df['"1st_chord"'],
                y=df['"2nd_chord"'])