#importing datetime library to get the correct current date
from datetime import datetime

#asking for exact birth date
day = int(input("Enter birth day (DD): "))
month = int(input("Enter birth month (MM): "))
year = int(input("Enter birth year (YYYY): "))

#converting to right format
birth_date = datetime(year, month, day)
current_date = datetime.now()

#calculating exact age difference
difference = current_date - birth_date

#calculating age in years, months, secs, days, and mins
age_years = difference.days // 365
age_months = difference.days // 30
age_days = difference.days
age_hours = difference.days * 24
age_minutes = age_hours * 60

print("Current Age:", age_years)
print("Current Age in months (approx):", age_months)
print("Current Age in days (approx):", age_days)
print("Current Age in hours:", age_hours)
print("Current Age in minutes:", age_minutes)
print("Years until 100:", 100 - age_years)