import os
import seaborn as sns

os.makedirs('data', exist_ok=True)

df = sns.load_dataset('titanic')

df.to_csv('data/titanic.csv')