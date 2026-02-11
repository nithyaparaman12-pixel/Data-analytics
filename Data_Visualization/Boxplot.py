import matplotlib.pyplot as plt

# Sample Data
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90,
         35, 40, 48, 52, 67, 73, 77, 82, 88, 92]

# Create Boxplot
plt.boxplot(marks)

# Add Title and Labels
plt.title("Student Marks Boxplot")
plt.ylabel("Marks")

# Show Grid
plt.grid(True)

# Show Plot
plt.show()
