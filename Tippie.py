#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

# Welcome text and bill amount
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))

# Ask the tip percentage
tip = int(input("What percentage tip would you like to give 10, 12, 15? "))

# How many in the group
people = int(input("How many people to split the bill? "))

# Calculate the bill total including % tip
bill +=  (bill * (tip / 100))

# Calculate the amount per person and show the result
amt_per_person = round(bill / people, 2)

# Always print 2 decimal places
total_pp = "{:.2f}".format(amt_per_person)    
print(f"Each person should pay: ${total_pp}")
