"""
1. Create an electricity bill estimator
2. Modify the bill estimator by asking the user to choose which tariff they are using
"""

"""Electricity Bill Estimator"""
# Cents_per_KWh = float(input("Enter cents per kWh: "))
# Number_of_KWh_used_per_day = float(input("Enter daily use in KWh: "))
# Number_of_days_in_billing_period = int(input("Enter number of billing days: "))
# Estimated_bill = Cents_per_KWh/100 * Number_of_KWh_used_per_day * Number_of_days_in_billing_period
# print("Estimated bill: ${:.2f}".format(Estimated_bill))

"""Electricity Bill Estimator 2.0"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff_choice = int(input("Which tafiff? 11 or 31: "))
Number_of_KWh_used_per_day = float(input("Enter daily use in KWh: "))
Number_of_days_in_billing_period = int(input("Enter number of billing days: "))
if tariff_choice == 11:
    Estimated_bill = TARIFF_11 * Number_of_KWh_used_per_day * Number_of_days_in_billing_period
else:
    Estimated_bill = TARIFF_31 * Number_of_KWh_used_per_day * Number_of_days_in_billing_period

print("Estimated bill: ${:.2f}".format(Estimated_bill))