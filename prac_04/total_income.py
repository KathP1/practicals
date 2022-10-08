"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """Print report showing income per month and cumulative income"""
    print("\nIncome Report\n-------------")
    total = 0
    # We already have the list of incomes, so we can iterate through that
    # enumerate adds a counter, in this case it's called month. We want the counter to start at 1
    for month, income in enumerate(incomes, 1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
