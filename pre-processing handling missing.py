import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.datasets import load_diabetes

ds = pd.read_csv('student1.csv')

X = ds[['Rank']].values
print("\nInput (Rank Column):\n", X)

imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

print("\nRank after Mean Imputation:\n", X)

db = load_diabetes()
df_db = pd.DataFrame(db.data, columns=db.feature_names)

print("\nDiabetes Dataset Head:\n", df_db.head())

sns.boxplot(x=df_db['bmi'])
plt.title("Outlier Detection using BMI")
plt.show()

print("\nOutliers in BMI:")
print(np.where(df_db['bmi'] > 0.12))
