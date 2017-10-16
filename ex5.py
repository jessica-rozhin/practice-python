"""
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extra:
Randomly generate two lists to test this
"""
import random

#function to generate a list
def list_generate():
    #pick list length
    list_gen = range(1, random.randint(5, 20))
    list = []
    for i in list_gen:
        list.append(random.randint(1, 99))
    return list

#function to check two lists and create a new list with their overlap
def check_overlap(a, b):
    #remove duplicates
    check_set = set(a)
    overlap_list = []
    for i in check_set:
        if i in b:
            overlap_list.append(i)
    return overlap_list

list_a = list_generate()
list_b = list_generate()
overlap_list = check_overlap(list_a, list_b)

print("\nHere are two randomly generated lists: ",'\n', list_a, '\n', list_b)

print("The following numbers are in both lists: ",'\n', overlap_list, '\n')
