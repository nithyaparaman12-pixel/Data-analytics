import matplotlib.pyplot as plt

# Sample Data (Student Marks)
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 
         35, 40, 48, 52, 67, 73, 77, 82, 88, 92]

# Create Histogram
plt.hist(marks, bins=5)

# Add Title and Labels
plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

# Show Grid
plt.grid(True)

# Show Chart
plt.show()
