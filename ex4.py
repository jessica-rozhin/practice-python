"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
"""
number = int(input("\nPlease enter a number >>> "))

poss_div = range(1, number+1)

div_list = []
for i in poss_div:
    if number%i ==0:
        div_list.append(i)

print(f"{number} is evenly divisible by the following numbers: ")
for i in div_list:
    print("\t", i)
