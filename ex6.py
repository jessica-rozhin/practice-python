"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
"""
def check_palindrome(string):
    reverse_string = string[::-1]
    if string == reverse_string:
        print("That is a palindrome!")
    else:
        print("That is NOT a palindrome.")

string = (str((input("Enter a string to check if it is a palindrome >>> ")))).lower()
check_palindrome(string)
