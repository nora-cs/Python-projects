#Write a function called duplicates that takes a list as the argument and returns a second list containing all duplicate items 
#So if give the list [2, 3 , 4, 4, 3, 1, 8, 0, 9]  it should return [3,4]
#Also test with ['pig', 'goat', 'cow', 'pig']

list_of_numbers = [2, 4, 6, 2, 6]
def duplicates(list_of_numbers):
    l=[]
    for i in list_of_numbers:
        x=list_of_numbers.count(i)
        if x >= 2:
            l.append(i)
            l=set(l)
            l=list(l)
            return l
        list_of_duplicates=duplicates(list_of_numbers)
        print(list_of_duplicates)
        
        list_of_animals = ['pig', 'goat', 'cow', 'pig']
        def duplicates()
            
    
#Write a Python program that matches a string that has an 'a' followed by zero or more 'b's
#Your code should be able to work on any provided string. Write the code to prove your function works
string = "abbb"
import re
match = re.search(r'^ab*$', string)

#Write a Python program that matches a string that has an 'a' followed by three 'b's.
#Like with the previous exercise, write the code to prove your work or code works 
string = "abbb"
match = re.search(r'^ab{3}$', string)


#Write a Python program that matches a word containing 'z'.
#Write the code to prove that your function works 
word = "zebra"
match = re.search(r'\w*z\w*', word)

# Write a Python program to search some literals strings in a string.
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox', 'dog', 'horse'

#If provided with the list below: 
str="""
>Venues
>Marketing
>medalists
>Controversies
>Paralympics
>snowboarding
>[1]
>Netherlands
>[2]
>Norway
>[10]
>[11]
>References
>edit
>[12]
>Norway
>Germany
>Canada
>Netherlands
>Japan
>Italy
>Belarus
>China
>Slovakia
<$#%#$%
<#$#$$
<**&&^^
>Slovenia
>Belgium
>Spain
>Kazakhstan
>[15]
>1964
>1968
>1972
>1992
>1996
>2000"""

#write some code to keep only the lines that start with a number or a letter after the > sign
match = re.search(r'[a-zA-Z0-9].*', str )



