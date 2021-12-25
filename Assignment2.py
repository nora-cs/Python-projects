#first things first, since y'all did not get it the last time. Copy Everything on this page into a #file and name it with a .py extension
#This ultimately means that whatever you send me should be executable

#Identify the type of each of the following variables and write it as a comment next to the variable
a  type(299) #int 
b  type(90.0) #float
c type(145")  #str
d type("\u0CA0_\u0CA0") #str
e type("True") #str
f type(True) #bool
g type(len('Sample') #int
h type(100**30) #int
i type(1 >= 1) #bool
j type(30%7) #int
k type(30/7) #float
l type(b + 7) 
   b = 4
   print(4+7)  #int
m type(128 << 1) #int
n type(bin(255) #str
o type([k, l, m, n ]) #int
p type(len(o))  #
  o = "christmas"
  type(len(o)) #int
    
#What value is at the end of the varialbe my_var at the end of these assignments. Add a comparison after the last statement
#in the form of my_val ==
my_var = 99
print(my_var)
my_var += 11
print(my_var)
my_var = str(my_var)
print(my_var)
my_var *= 2
print(my_var)
my_var = len(my_var)
print(my_var)
my_var *= 4
print(my_var)
if my_val == 35:
   print("my_val is 35")
else: 
   print(number)

#Change the loop below so that it prints the numbers from 1 to 10
range(1,11)
for i in range(11)
print(i)

#Save a copy of your favorite snack as a variable. Using that variable, print your favorite snack 100 times

snack = "popcorn"
print((snack + " ") * 100)

#Make a list of your grocery items with prices 9.42, 5.67, 3.25, 13.40, 7.50 and store it as a variable. Using a builtin function, #find the cheapest and the most expensive items on your shopping list


list = {'rice': 9.42, 'meat': 13.40, 'carrots': 5.76, 'chips': 3.25, 'oil': 7.50 }
Print(list)
list1,  list2 = [ 'rice', 'meat', 'carrots', 'chips', 'oil' ], [ 9.42, 13.40, 5.76, 3.25, 7.50 ]

print("Max value element : ", max(list1))

print("Max value element : ", max(list2))



#Import random. run dir(random.randint). Use Randint to randomly print between 0 and 100 copies of your favorite snack

import random
dir(random.randint)

#Run dir(random). Find a function in random that you can use to print a random item from your grocery list. Remember you can use #help to find out what functions do.

#Write code to randomly select items from your groceries list, round them to the nearest integer and print the result

#Previously,we used the * operator to print a hundred copies of your favorite snack. This time use a while loop to print 50 copies of your favorite snack.

#Mix and Match! Write a while loop that uses the * operator to print multiple copies of your favorite snack per line. Print out 10 lines where the first line has one copy of your favorite snack and the last line hast 10.

#Challenge: Your neighborhood grocery store is having a weird promotion called "Win free change". A random item is picked from your #grocery list and you pay 10 dollars. If the item is less than 10 dollars, you get the item and the balance from the items price. If #the item is more than 10 dollars, you get the item and the difference in the price as change. Write the code to randomly pick a #price from your price list and print out the amount the cashieri
