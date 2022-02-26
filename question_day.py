#Wed-29th

1. for num in range(2,-5,-1):
              print(num, end=", ")
2, 1, 0, -1, -2, -3, -4,

2.  if a > 0:
    if b < 0:
       x = x + 5
  elif a > 5:
       x = x + 4
  else: 
      x = x + 3
  else:
      x = x + 2
      print(x) 


3. for num in range(10, 14):
       for i in range(2, num):
       if num%i == 1:
          print(num)
         break
   10
   11
   12
   13

4. if a + b:
      print('True')
   else:
      print('False')
True


5.var = 10
      for i in range(10):
       for j in range(2,10,1):
        if var % 2 == 0:
         conitinue
         var += 1
          var += 1
     else:
        var += 1
        print(var)
*********************************************************************************

#Thursd-30th:

# What is the output of print(2 ** 3 ** 2)

512 

#What is the output of: 
print(10 - 4 * 2)

2

# What is the value of the following Python Expression
print(36 / 4)

9.0

# What is the output of the following Python code
x = 10
y = 50
if x ** 2 > 100 and y < 100:
        print(x, y)
?

# What is the output of the following code
        x = 100
        y = 50
        print(x and y)
50
# Monday Jan 10th
# 1. write a python function to find the max of 3 numbers.
def max_num(x,y,z):
     return max(x,y,z)
max_num(5,8,9)
#2. Write a python function to sum all the numbers in a list.
def sum_num(a,b,c,d):
    total = a+b+c+d
    return total
sum_num(1,2,3,4)
#3. Write a python function to multiply all numbers in a list
def multiply_num(a,b,c,d):
    total = a*b*c*d
    return total
multiply_num(1,2,3,4)
#4. Write a python function to reverse a given string.
def string(x):
   return x[::-1]
   print(string)
string('I love Python')
#5. Write a python function that takes a string and displays the number of upper case letters and the number of lower case letters.
def count_up_and_low(string):
     u = [i for i in string if i.isupper()]
     l = [i for i in string if i.islower()]
     return len(u), len(l)
count_up_and_low('I Love Python')

#January 11th 

#So for example if func(23, 25, 25)
#it should print 23, 25, and 25,
#if func(20, 21)
#it should print 20, 21
+#Also, it must return both addition and subtraction in a single return call.
#Write a program to create a function show_employee() using the following conditions.
#It should accept the employee’s name and salary and display both.
#If the salary is missing in the function call then assign default value 9000 to salary

#January 12th
#Write a shut_down functioon that takes one argument. if the argument is yes, the function should return shutting down, if no it should return shut down aborted. if the argument is neither yes or no, the function should return sorry.
def shut_down(x):
 for i in  x:
  if  i in x:
        print(i, 'shutting down')
  elif   print(i, 'shut down aborted'):
  else:
        print('sorry')
  shut_down()      
#Define a function called hotel_cost with one argument nights as input. The hotel costs $140 per night. So, the function hotel_cost should return 140 * nights.
#Define a function called plane_ride_cost that takes a string, city, as input. The function should return a different price depending on the location.
#define a function called rental_car_cost with an argument called days. Calculate the cost of renting the car: Every day you rent the car costs $40.(cost=40*days) if you rent the car for 7 or more days, you get $50 off your total(cost-=50). Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total. You cannot get both of the above discounts. Return that cost.
#Now define a function called trip cost that takes the output from the three functions above and prints the total cost of the trip
#First, def a function called distance_from_zero, with one argument (choose any argument name you like). If the type of the argument is either int or float, the function should return the absolute value of the function input. Otherwise, the function should return "Nope". Check if it works calling the function with -5.6 and "what?".


 #January 17th 2022
 
#1. Which of the following is an operator and which is a value
* #operator
'Hello' #value
-88.88  #value
- #operator
/  #operator
+  #operator
5  #operator
#2. Which of these is a variable and which is a string
 spam #variable
'spam' #string
#3. Name three data types 
 floats, intergers, strings
#4. what is an expression made of. What do all expressions do?
 A specific sequence of characters that help you match and find other strings by evaluating them 
#5. What does the variable bacon contain after running the the code below
bacon = 20
bacon + 1
21

#Jan. 19th

#What are the two values of a boolean data type. How do you write them. 
True = 1, False = 0
#What are the three boolean operators? 
and, or , not
#Write out the truth tables of both boolean operators i.e every possible combination of boolean values and their result. 
and	True if both are true	a and b
or	True if at least one is true	a or b
not	True only if false
#What are the six comparison operators. 
Less than(<), Greater that(>), Less than or equal to(<=), Greater than or equal to (>=), Equal to(==), Not equal to(!=)
#What is the difference between the equal operator and the assignment operator
the equal operator(=)is used to assign value to a variable and the assignment operator (==)is used to compare two variable or constants

# Why are functions advantages to have in your programs
To better organize our code
# When does the code in a function get executed, when its defined or when it is called ??
When it's called
#. what statement creates a function
def
# if a function does not have a return value, what is the return value when the function is called??
A default value
# How can you prevent a program from crashing if it runs into an error
Trying your code without printing it 
  

# Monday 24th

#Why is eggs a valid variable but 100 is not?
 because 100 begins with a number

#what 3 functions can be used to get the integer, floating point number or string version of a value
 The int(), float(), and str() functions
#Why does the following expression result in an error? How can you fix it.
'I have eaten ' + 99 + ' burritos'
put quotes around 99 to treat it as a string because all the other phrases are strings

#if you have a function named fufu() inside of a module named lunch, how will you call it after importing lunch?
Use the CALL FUNCTION statement to call it 

#what goes in the try clause, what goes in the except clause of a function
The try clause will execute as long as there is no exception/error where as the except clause will execute if there is an exception or error in the code

#January 31st 

#when we talk about relative paths, what is the relative path relative to??
The location that is relative to a current directory
#What does an absolute path start with??
 (/) symbol
#what are the 3 mode arguments that can be passed to the open() function??
r : Opens the file in read-only mode. ...
rb : Opens the file as read-only in binary format and starts reading from the beginning of the file. ...
r+ : Opens a file for reading and writing, placing the pointer at the beginning of the file.
#What happens if an existing file is opened in write mode??
 It creates an empty file for output operations
#what is the difference between the read() and the readlines() methods??
The read() method returns the specified number of bytes from the file whileThe readline() function reads from a file in read mode and returns the next line in the file or a blank string if there are no more lines 
 
 # February 1st 2022:
 
 #what is the function that creates regex objects
 The re. compile() function
 #Why are raw strings often used when creating regex objects
 So backslashes do not have to be escaped.
 #What does the search() method return?
 A match object if there is a match, returns a "none" value if no matches are found
 #In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? group1?, group2?
 Group 0 is the entire match, group 1 covers the first set of parentheses, and group 2 covers the second set of parentheses.
 #Parentheses and periods have specific meanings in regular expressions. How will you specify that you want a regex to match actual parenthesis and period characters?
 use a / slash


