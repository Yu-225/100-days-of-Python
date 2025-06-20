"""Tip calculator"""

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15? ")
)
people = int(input("How many people to split the bill? "))

bill_with_tip = total_bill + (tip_percentage / 100 * total_bill)
bill_per_person = bill_with_tip / people

print(f"Each person should pay: ${bill_per_person:.2f}")
