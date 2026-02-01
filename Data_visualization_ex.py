import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "March", "April"],
    "Expense": [20000, 45000, 28000, 35000]
}

df = pd.DataFrame(data)

plt.bar(df["Month"], df["Expense"])
plt.title("Monthly Expenses")
plt.xlabel("Month")
plt.ylabel("Expense")
plt.show()
