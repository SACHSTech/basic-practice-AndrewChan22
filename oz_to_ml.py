'''
-------------------------------------------------------------------------
Name:		oz_to_ml.py
Purpose:	oz to mL calculator

Author:	Chan. A

Created:	date in 12/02/2020
-------------------------------------------------------------------------
'''
# Introduction
print("Welcome to the Oz to mL converter")

# Asks user for # of ounces
ounces = float(input("Enter the amount of fluid in ounces: "))

# Asks user for # of people (serving)
people = int(input("Enter the number of people to serve: "))

# Converts ounces to mL
convert = ounces * 29.5735

# Divides # of people by recipe serving size
serving_size = people/4

# Final Calculation
print("You will need " + str(convert * serving_size) + " mL.")