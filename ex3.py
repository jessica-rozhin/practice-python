"""
Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:
A) Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
B) Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
"""
import random

list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def basic_solution(l):
    print("Here are the list elements that are less than 5: ")
    for i in l:
        if i < 5:
            print(i)
    return

def extra_a(l):
    print("Here is a new list, with only number less than 5: ")
    new_list = []
    for i in l:
        if i < 5:
            new_list.append(i)
    print(new_list)
    return new_list

def extra_b(l):
    number = int(input("Please pick a number between 1 and 99: "))
    new_list = []
    for i in l:
        if i < number:
            new_list.append(i)
    print(new_list)
    return new_list

basic_solution(list)
extra_a(list)
extra_b(list)
