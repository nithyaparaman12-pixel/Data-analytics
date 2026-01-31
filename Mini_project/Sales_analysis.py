import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1️⃣ CREATE SAMPLE DATA
# -----------------------------
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [20000, 25000, None, 30000, 28000, 500000],  # outlier + missing
    "Customers": [120, 150, 130, None, 160, 170]
}

df = pd.DataFrame(data)

print("---- ORIGINAL DATA ----")
print(df)

# -----------------------------
# 2️⃣ DATA INFO CHECK
# -----------------------------
print("\n---- DATA INFO ----")
df.info()

# -----------------------------
# 3️⃣ MISSING VALUE CHECK
# -----------------------------
print("\n---- MISSING VALUES ----")
print(df.isnull().sum())

# -----------------------------
# 4️⃣ MISSING VALUE HANDLING
# -----------------------------
df["Sales"] = df["Sales"].fillna(df["Sales"].median())
df["Customers"] = df["Customers"].fillna(df["Customers"].median())

print("\n---- AFTER MISSING VALUE HANDLING ----")
print(df)

# -----------------------------
# 5️⃣ OUTLIER DETECTION (IQR)
# -----------------------------
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["Sales"] < lower) | (df["Sales"] > upper)]

print("\n---- SALES OUTLIERS ----")
print(outliers)

# -----------------------------
# 6️⃣ NUMPY CALCULATIONS
# -----------------------------
sales_array = np.array(df["Sales"])

print("\n---- NUMPY STATS ----")
print("Average Sales:", np.mean(sales_array))
print("Max Sales:", np.max(sales_array))
print("Min Sales:", np.min(sales_array))

# -----------------------------
# 7️⃣ VISUALIZATION
# -----------------------------

# Line chart - Sales Trend
plt.plot(df["Month"], df["Sales"])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.show()

# Bar chart - Customers per Month
plt.bar(df["Month"], df["Customers"])
plt.xlabel("Month")
plt.ylabel("Customers")
plt.title("Customers per Month")
plt.show()

# Boxplot - Outlier detection
plt.boxplot(df["Sales"])
plt.title("Sales Outlier Detection")
plt.ylabel("Sales")
plt.show()
