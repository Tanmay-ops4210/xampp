import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler, MinMaxScaler

iris = load_iris()

data = pd.DataFrame(
    data=np.c_[iris['data'], iris['target']],
    columns=iris['feature_names'] + ['target']
)

numerical_features = iris['feature_names']
X = data[numerical_features]
y = data['target']

scaler_standard = StandardScaler()
X_standardized = scaler_standard.fit_transform(X)

scaler_minmax = MinMaxScaler()
X_normalized = scaler_minmax.fit_transform(X)

plt.figure(figsize=(12, 4))

plt.subplot(131)
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y, cmap='viridis')
plt.title('Original Features')

plt.subplot(132)
plt.scatter(X_standardized[:, 0], X_standardized[:, 1], c=y, cmap='viridis')
plt.title('Standardized Features')

plt.subplot(133)
plt.scatter(X_normalized[:, 0], X_normalized[:, 1], c=y, cmap='viridis')
plt.title('Normalized Features')

plt.tight_layout()
plt.show()
