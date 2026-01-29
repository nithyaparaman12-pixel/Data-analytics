import pandas as pd

# Sample data
data = {
    "Name": ["Arun", "Divya", "Karthik", "Meena", "Suresh"],
    "Maths": [78, 85, None, 90, 66],
    "Science": [72, None, 88, 91, 70],
    "English": [80, 75, 82, None, 68]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Data")
print(df)

# Check missing values
print("\nMissing Values")
print(df.isnull().sum())

# Fill missing values with subject mean
df["Maths"].fillna(df["Maths"].mean(), inplace=True)
df["Science"].fillna(df["Science"].mean(), inplace=True)
df["English"].fillna(df["English"].mean(), inplace=True)

# Total & Average
df["Total"] = df["Maths"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

# Result column
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 50 else "Fail")

print("\nCleaned & Analyzed Data")
print(df)

# Topper
topper = df.loc[df["Average"].idxmax()]
print("\nTopper Details")
print(topper)
