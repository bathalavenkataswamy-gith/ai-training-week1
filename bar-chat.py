from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
employees_path = BASE_DIR / "employees.csv"

employees = pd.read_csv(employees_path)

average_salary = (
    employees.groupby("department", sort=True)["salary"].mean().sort_values(ascending=False)
)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
monthly_sales = [12, 15, 14, 18, 22, 25]


def save_bar_chart():
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(average_salary.index, average_salary.values, color="steelblue")
    ax.bar_label(
        bars,
        labels=[f"{value:,.0f}" for value in average_salary.values],
        padding=3,
    )
    ax.set_title("Average Salary per Department")
    ax.set_xlabel("Department")
    ax.set_ylabel("Average Salary")
    ax.set_ylim(0, average_salary.max() * 1.15)
    fig.tight_layout()
    fig.savefig(BASE_DIR / "bar_avg_salary.png", dpi=150)
    plt.close(fig)


def save_histogram():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(employees["salary"], bins=5, color="seagreen", edgecolor="black")
    ax.set_title("Salary Distribution")
    ax.set_xlabel("Salary")
    ax.set_ylabel("Number of Employees")
    fig.tight_layout()
    fig.savefig(BASE_DIR / "hist_salary.png", dpi=150)
    plt.close(fig)


def save_scatter_plot():
    fig, ax = plt.subplots(figsize=(8, 5))
    for department, group in employees.groupby("department"):
        ax.scatter(
            group["id"],
            group["salary"],
            label=department,
            s=60,
        )
    ax.set_title("Employee ID vs Salary by Department")
    ax.set_xlabel("Employee ID")
    ax.set_ylabel("Salary")
    ax.legend(title="Department")
    fig.tight_layout()
    fig.savefig(BASE_DIR / "scatter_id_salary.png", dpi=150)
    plt.close(fig)


def save_line_chart():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(months, monthly_sales, marker="o", color="darkorange")
    ax.set_title("Monthly Sales (Jan-Jun)")
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(BASE_DIR / "line_monthly_sales.png", dpi=150)
    plt.close(fig)


def save_combined_chart():
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))

    ax = axes[0, 0]
    bars = ax.bar(average_salary.index, average_salary.values, color="steelblue")
    ax.bar_label(
        bars,
        labels=[f"{value:,.0f}" for value in average_salary.values],
        padding=2,
        fontsize=8,
    )
    ax.set_title("Average Salary per Department")
    ax.set_xlabel("Department")
    ax.set_ylabel("Average Salary")

    ax = axes[0, 1]
    ax.hist(employees["salary"], bins=5, color="seagreen", edgecolor="black")
    ax.set_title("Salary Distribution")
    ax.set_xlabel("Salary")
    ax.set_ylabel("Employees")

    ax = axes[1, 0]
    for department, group in employees.groupby("department"):
        ax.scatter(group["id"], group["salary"], label=department, s=45)
    ax.set_title("Employee ID vs Salary")
    ax.set_xlabel("Employee ID")
    ax.set_ylabel("Salary")
    ax.legend(title="Department", fontsize=8)

    ax = axes[1, 1]
    ax.plot(months, monthly_sales, marker="o", color="darkorange")
    ax.set_title("Monthly Sales")
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(BASE_DIR / "combined_charts.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    save_bar_chart()
    save_histogram()
    save_scatter_plot()
    save_line_chart()
    save_combined_chart()
    print("Saved 4 required charts and 1 bonus combined chart.")