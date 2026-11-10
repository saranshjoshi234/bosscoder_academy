# Question 1: Write a Python function that checks 
# if a given string is a palindrome. 
# A palindrome is a word, phrase, number, 
# or other sequence of characters that reads the same forward and backward. 
# The function should return `True` if the string is a palindrome and `False` 
# otherwise.

def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("abdba"))
