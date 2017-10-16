"""Let’s say I give you a list saved in a variable:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
"""
import random

#simple version
#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#a_even = []
#for i in a:
#    if i%2 == 0:
#        a_even.append(i)
#print(a_even)

#function to generate a list
def list_generate():
    list_gen = range(1, random.randint(5, 20))
    list = []
    for i in list_gen:
        list.append(random.randint(1, 99))
    return list

def remove_odds(list):
    new_list = []
    for i in list:
        if i%2 == 0:
            new_list.append(i)
    return new_list

list = list_generate()
print("\nHere is your randomly generated list: ", list)
even_list = remove_odds(list)
print("Here is a list of only the even numbers: ", even_list, "\n")
