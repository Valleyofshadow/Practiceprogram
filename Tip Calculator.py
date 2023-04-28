print("Welcome to the tip calculator")
bill = int(input("How much was the total bill?\n"))
tip = (int(input("what percentage tip would you like to give?\n"))/100) + 1
people = int(input("How many people will be splitting the bill?\n"))
cost = str((bill * tip) / people)
print ("Each person should pay: $" + cost)