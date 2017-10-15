"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
A) Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
B) Print out that many copies of the previous message on separate lines.
http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
"""
import datetime

#user inputs
name = input("\nWhat is your name? >>> ")
age = int(input("What is your age? >>> "))

#get current year
now = datetime.datetime.now()
current_year = now.year

#calulate future year
future_year = (100 - age) + current_year

#give answer
print(f"\n{name} will be 100 years old in {future_year}.")

#extra A & B
number = int(input(f"Would you please input another number? >>> "))
print(f"\n{name} will be 100 years old in {future_year}." * number)
