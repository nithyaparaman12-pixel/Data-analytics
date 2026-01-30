import pandas as pd

# Sample Data
data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [25, None, 30, None],
    "Salary": [30000, 40000, None, 50000],
    "City": ["Chennai", None, "Madurai", "Coimbatore"]
}

df = pd.DataFrame(data)

#  Missing values per column
print("Missing values count per column:")
print(df.isnull().sum())

# Check if any missing values exist
print("\nAny missing values present?")
print(df.isnull().values.any())

# Total missing values in dataset
print("\nTotal missing values:")
print(df.isnull().sum().sum())

# Show rows which contain missing values
print("\nRows with missing values:")
print(df[df.isnull().any(axis=1)])
