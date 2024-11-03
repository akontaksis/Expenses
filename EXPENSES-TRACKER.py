import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def visualize_spending_by_category(month):
    category_summary = spending_by_category(month)
    category_summary.plot(kind="pie", autopct="%1.1f%%")
    plt.title(f"Spending by Category for Month {month}")
    plt.ylabel("")
    plt.show()

def spending_by_category(month):
    expenses = pd.read_csv("expenses.csv", names=["Date", "Category", "Amount"])
    expenses["Date"] = pd.to_datetime(expenses["Date"])
    monthly_expenses = expenses[expenses["Date"].dt.month == month]
    
    category_summary = monthly_expenses.groupby("Category")["Amount"].sum()
    print("Spending by Category:")
    print(category_summary)
    return category_summary

def calculate_monthly_summary(month, income=0):
    expenses = pd.read_csv("expenses.csv", names=["Date", "Category", "Amount"])
    expenses["Date"] = pd.to_datetime(expenses["Date"])
    print(expenses)
    monthly_expenses = expenses[expenses["Date"].dt.month == month]
    
    total_spent = monthly_expenses["Amount"].sum()
    savings = income - total_spent
    
    print(f"Total spent: ${total_spent:.2f}")
    print(f"Savings: ${savings:.2f}")
    return total_spent, savings

def view_expenses():
    try:
        expenses = pd.read_csv("expenses.csv", names=["Date", "Category", "Amount"])
        print(expenses)
    except FileNotFoundError:
        print("No expenses found. Add some expenses first!")

def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., groceries, entertainment, transportation): ")
    amount = float(input("Enter the amount: "))
    
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("Expense added successfully!")

def delete_last_reord():
        
    try:   
        # Read the existing expenses data
        expenses = pd.read_csv("expenses.csv", names=["Date", "Category", "Amount"])
        
        if expenses.empty:
            print("No records found to delete.")
            return
        # Drop the last row
        expenses = expenses[:-1]
         # Save the updated DataFrame back to the CSV
        expenses.to_csv("expenses.csv", index=False, header=False)
        print("Last record deleted successfully!")
    
    except FileNotFoundError:
        # Error if the CSV file doesn't exist
        print("No expense file found. Please add some expenses first.")
    
    except Exception as e:
        # General error handling for other potential issues
        print(f"An error occurred: {e}")


def main():
   
    print("Welcome to the Expense Tracker!")
    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Spending by Category")
        print("5. Visualize")
        print("6. Delete the last Record")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            month = int(input("Enter the month number (1-12): "))
            income = float(input("Enter your monthly income: "))
            calculate_monthly_summary(month, income)
        elif choice == "4":
            month = int(input("Enter the month number (1-12): "))
            spending_by_category(month)
        elif choice == "5":
            month2 = int(input("Enter the month number (1-12): "))
            visualize_spending_by_category(month2)
        elif choice == "6":
            delete_last_reord()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

