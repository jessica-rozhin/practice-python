"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

Extras:
A) If the number is a multiple of 4, print out a different message.
B) Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
#general solution and extra A
number = int(input("\nPlease pick a number >>> "))

if number%4 == 0:
    print("That number is divisible by four (and is even).")
elif number%2 == 0:
    print("That number is even.")
else:
    print("That number is odd.")

#extra B
print("\nPlease pick two numbers: ")
number_a = int(input(">>> "))
number_b = int(input(">>> "))

if number_a%number_b == 0:
    print(f"{number_a} is evenly divisible by {number_b}")
else:
    print(f"{number_a} is not evenly dividiable by {number_b}")
