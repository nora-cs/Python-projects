# if we list all numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these numbers is 23.
# Write some code to find the sum of all  multiples of 3 and 5 between 0 and 1000.
sum(n for n in range(1000) if n % 3 == 0 or n % 5 == 0)
#Write a python program to count the number of occuring characters in a given string.
#Sample String : google.com'
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
from collections import Counter
string = "I love Python"
Counter(string)
#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'
string = "people"
print(string[:1]+string[1:].replace(string[0],"$"))
#Given the following list, list1 = [100, 200, 300, 400, 500], reverse the list
#expected result: [500, 400, 300, 200, 100]
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)
#Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
#so if given:
#list1 = ["M", "na", "i", "Ke"]
#list2 = ["y", "me", "s", "lly"]
#Expected output should be: ['My', 'name', 'is', 'Kelly']
list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
combined_list = [i + n for i, n in zip(list1, list2)]
print(combined_list)
# Write a Python program to iterate over dictionaries using for loops.
dict = { 'a':'elders', 'b':'children', 'c':'adults', }
for key, value in dict.items():
    print(key, value)
#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
#Sample Dictionary ( n = 5) :
#Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
n = 10
dict = {x: x * x for i in range(1, n * 1)}
print(dict) 
#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
d = dict()
for x in range(1,16):
    d[x]=x**2
    print(d)

#Assign the first number of lst to answer _1 and print it. I have helped  you with some of the code
lst=[11, 100, 99, 1000, 999]
answer_1=
lst= [11, 100, 99, 100,999]
In [150]: answer_1 = lst[0]
In [151]: print(answer_1)

#Now print the second item directly. again I am helping you with some of the code
lst=[11, 100, 99, 1000, 999]
print()