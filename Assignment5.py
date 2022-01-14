#Write a function called all_the_snacks that takes one argument. Use the * operator to print that snack 100 times.
def all_the_snacks(x):
    print(x *100)
all_the_snacks("popcorn")
#Test your function using multiple items from your grocery list. If you don't have a grocery list, this would be a good time to
#create one
grocery_list = [ 'sugar', 'bread', 'butter' ]
def all_the_snacks(a, b, c):
    print(a + b + c)
all_the_snacks('sugar', 'bread', 'butter')  
#You notice that your all_the_snacks prints your snacks all squished together. Rewrite the function to take a second argument, #called spacer which we will use to put some space between the snack items. Try your rewritten function with multiple inputs
def all_the_snacks(a, b, c):
    print(a + " " + b  + " " + c)
all_the_snacks('sugar', 'bread', 'butter')
#Rewrite your all_the_snacks function so that it takes an additioanl argument called num. Use this variable to customize how many #times your snack is printed out.
#Write a price_matcher function that takes no arguments but prints a random item from your grocery list everytime it is run.
def price_matcher():
value = random.choice(grocery_list)
for i in grocery_list:
  if i in grocery_list:
      print(i)
#Write an in_grocery_list function that takes a grocery list and prints true if the item is on your grocery list and false if #otherwise
def in_grocery_list(x):
  for i in grocery_list:
if i in grocery_list:
         print(i, "true")
else:
        print(i, "false")
in_grocery_list('butter')
#Write the all the snacks function so that num and spacer have default values of 100 and ',' respectively.
#Challenge: use input to get your neighbors favorite color and store it as a variable.
fav_color = input("Enter fav color: " )
print(fav_color)
#Write an april_fools_color_swapper that uses input to get your favorite color, uses input to get your neighbors color and then prints them with your name and your neighbor's name. On the next line, it should swap your color for your neighbors color and print them.
#Create a function called shout which ask a user for their name and shouts it back to them
#So if the user is called Nora, your function should print HELLO NORA!
def shout():
   name=str(input("enter name : "))
   print(str(name))
   return
shout()






