#Write a python function that takes one argument, which is a list and swaps the first and last items on that list

list = [ 3, 5, 9, 11 ]
def list(newlist):
    list[0], list[-1] = list[-1], list[0]
    list
    
#Write the code that allows you to show that your function works as it should
#Write a python function that takes one argument which is a string and reverses the order of the words in the string.
def word(string):  
    word = string.split(' ') 
    rev = ' '.join(reversed(word)) 
    return rev
 
s= "I love python"
print ("reverse: " ,rev_words(s))

# Create a dictionary and display its keys alphabetically.
from collections import OrderedDict
 
dict = {'marie':'1','joy':''2','tom':'3','lem':'4'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)
#Display both the keys and values sorted in alphabetical order by the key.
#Same as part (ii), but sorted in alphabetical order by the value.
#Write a python function called doings that takes one argument named number. if number is even, doings should print dividing number by 2, divide number by two and return the answer. if number is odd, the function should print, multiplying number by 3 and adding one, then multiply number by 3 and add one to it and return that result. Then write a function that allows a user to enter the numbers that get passed to the doing function. It should keep asking for the number as long as the result of doings is not 1.
#Write two functions. One should use a for loop to print the numbers between 1 and 100. The second should use a while loop to print the numbers between 1, and 100.
def range()
for i in range(1, 100):
    print(i)
    
   def print_num(n):
        if n > 0:
        print_num(n - 1)
        print(n, end = ' ')

print('Numbers from 1 to 100:')
print_num(100) 
    
#Write a Python program to square and cube every number in a given list of integers using Lambda.
#Write a Python program to check whether a given string is number or not using Lambda.

contains_digit = False
string = "water1"
for character in string:
   if character.isdigit():
        contains_digit = True

print(contains_digit)






