import matplotlib.pyplot as plt
import pandas as pd

# 1. Create / load employees.csv (from Day 3)
data = """id,name,department,salary,city
1,Arun,Sales,30000,Chennai
2,Priya,HR,45000,Chennai
3,Rahul,IT,60000,Bangalore
4,Divya,IT,75000,Chennai
5,Karthik,Finance,90000,Mumbai
6,Meena,Sales,52000,Bangalore
7,Suresh,IT,68000,Chennai
8,Anitha,HR,48000,Mumbai
"""

with open("employees.csv", "w") as f:
    f.write(data)

df = pd.read_csv("employees.csv")

# 2. Bar chart: Average salary per department with labels & values on bars
dept_avg = df.groupby("department")["salary"].mean()

plt.figure(figsize=(7, 4))
bars = plt.bar(dept_avg.index, dept_avg.values)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

for bar in bars:
    val = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        val,
        f"{val:.0f}",
        ha="center",
        va="bottom",
    )

plt.tight_layout()
plt.savefig("bar_avg_salary.png")
plt.close()

# 3. Histogram: Salaries with 5 bins
plt.figure(figsize=(7, 4))
plt.hist(df["salary"], bins=5, edgecolor="black")
plt.title("Salary Distribution (5 Bins)")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("hist_salary.png")
plt.close()

# 4. Scatter plot: id vs salary coloured by department with legend
plt.figure(figsize=(7, 4))
for dept, group in df.groupby("department"):
    plt.scatter(group["id"], group["salary"], label=dept)

plt.title("Employee ID vs Salary by Department")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(title="Department")
plt.tight_layout()
plt.savefig("scatter_id_salary.png")
plt.close()

# 5. Line chart: Monthly sales (Jan to Jun) with markers
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(7, 4))
plt.plot(months, sales, marker="o", label="Monthly Sales")
plt.title("Monthly Sales (Jan - Jun)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.tight_layout()
plt.savefig("line_monthly_sales.png")
plt.close()

print("Saved all 4 charts successfully!")
print("Average salary per department:\n", dept_avg)