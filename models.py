# Heart Dataset Heatmap - Full Code

# 1. Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load the dataset
# Make sure 'heart.csv' is in the same folder as this script
df = pd.read_csv("heart.csv")

# 3. View first few rows
print("First 5 rows of the dataset:")
print(df.head())

# 4. Check dataset info
print("\nDataset Info:")
print(df.info())

# 5. Check if there are missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# 6. Calculate the correlation matrix
corr_matrix = df.corr()

# 7. Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    cbar=True
)
plt.title("Correlation Heatmap of Heart Dataset", fontsize=16)
plt.show()
