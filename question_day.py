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
















