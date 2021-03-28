# **Day 2**

<u>New code learned</u>

| Code                | Expanation                                                   | Method                                        |
| ------------------- | ------------------------------------------------------------ | --------------------------------------------- |
| **"{:.2f}".format** | How to format and show variable to two decimal places even if the second decimal place is zero | total_pp = "{:.2f}".format(amt_per_person)    |
| **F-string**        | Used method of combining a string and other variables in one displayed sentence | print(f"Each person should pay: ${total_pp}") |
| **Round**           | used for rounding up a number to a specified amount of decimal places. | amt_per_person = round(bill / people, 2)      |



# Explantion

Learned about the different sorts of variables. Python does not need variable declaration. Type of variable can be changed by putting the new type before the variable name.

**Int, float, Boolean, str**

 Method

people = int(input("How many people to split the bill? "))

# Explantion

Learned about the different sorts of calculations available. Python has a strict order of how it calculates a line of code.

**( ) * / + -**

 Method

bill += (bill * (tip / 100))