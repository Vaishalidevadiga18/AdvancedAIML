from tabulate import tabulate

# Data: Subjects and Marks
subjects = ["Mathematics", "DBMS", "Machine Learning", "Automata", "Computer Networks", "AI Lab"]
marks = [85, 90, 88, 80, 84, 92]

# Combine into rows
table = list(zip(subjects, marks))

# Display table
print("📘 Last Semester Marks Table:\n")
print(tabulate(table, headers=["Subject", "Marks"], tablefmt="fancy_grid"))

# Calculate total and percentage
total = sum(marks)
percentage = total / len(marks)

print("\nTotal Marks:", total)
print("Percentage:", round(percentage, 2), "%")
