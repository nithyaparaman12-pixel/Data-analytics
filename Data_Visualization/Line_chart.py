import matplotlib.pyplot as plt

# Sample Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [20000, 25000, 22000, 30000, 28000, 35000]

# Create Line Chart
plt.plot(months, sales, marker='o')

# Add Title and Labels
plt.title("Monthly Sales Analysis")
plt.xlabel("Months")
plt.ylabel("Sales Amount")

# Show Grid
plt.grid(True)

# Show Chart
plt.show()
