'''
-------------------------------------------------------------------------
Name:		cake_jog.py
Purpose:	uses user input to calculate km needed to burn off calories from a certain number of cakes

Author:	Chan. A

Created:	date in 12/02/2020
-------------------------------------------------------------------------
'''
# asks user for input
cake = int(input("How many pieces of cake have you eaten?: "))

# calculates how many km is needed to burn off a piece of cake
km_needed = (225/100) * cake

# final caluclation and statement
print("You will need to run " + str(km_needed) + "km to burn off the calories.")