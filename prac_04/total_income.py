"""
CP1404 - prac 04
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    income_list = []  # Renamed from 'incomes' to 'income_list'
    number_of_months = int(input("How many months? "))


    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))  # Using f-string
        income_list.append(income)

    print_report(number_of_months, income_list)

def print_report(number_of_months, income_list):
        """Print the income report."""
        print("\nIncome Report\n-------------")
        total = 0
        for month in range(1, number_of_months + 1):
            income = income_list[month - 1]
            total += income
            print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()
