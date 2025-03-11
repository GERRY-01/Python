 # A program that converts a given number of days into years, weeks and months

days = int(input("Enter the number of days: "))

years = days // 365
remaining_days = days % 365

months = remaining_days // 30
remaining_days = remaining_days % 30

weeks = remaining_days // 7
remaining_days = remaining_days % 7

print(f"{days} days is approximated to be {years} years, {months} months, {weeks} weeks and {remaining_days} days")

