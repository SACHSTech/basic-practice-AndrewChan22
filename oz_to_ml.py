print("Welcome to the Oz to mL converter")

ounces = float(input("Enter the amount of fluid in ounces: "))

people = int(input("Enter the number of people to serve: "))

convert = ounces * 29.5735
serving_size = people/4

print("You will need " + str(convert * serving_size) + " mL.")