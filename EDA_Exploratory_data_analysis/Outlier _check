import pandas as pd

# Sample data
data = {
    "Salary": [25000, 30000, 28000, 27000, 26000, 500000]
}

df = pd.DataFrame(data)

# Q1 and Q3
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

# IQR
IQR = Q3 - Q1

# Bounds
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print("Lower Bound:", lower)
print("Upper Bound:", upper)

# Outlier values
outliers = df[(df["Salary"] < lower) | (df["Salary"] > upper)]
print("\nOutliers:")
print(outliers)
