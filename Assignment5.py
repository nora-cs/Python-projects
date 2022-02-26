#Write a function called all_the_snacks that takes one argument. Use the * operator to print that snack 100 times.
def all_the_snacks(snack):
    return snack * 100
    snack = "popcorn"
    another_snack = "chips"
    all_the_snacks(snack)
    all_the_snacks(another_snack)
#Test your function using multiple items from your grocery list. If you don't have a grocery list, this would be a good time to
#create one
grocery_list = [ 'sugar', 'bread', 'butter' ]
for i in grocery_list:
    all_the_snacks(i)  
#You notice that your all_the_snacks prints your snacks all squished together. Rewrite the function to take a second argument, #called spacer which we will use to put some space between the snack items. Try your rewritten function with multiple inputs
def all_the_snacks_modified(snack, spacer):
           Print((snack + spacer) * 100) 
           for i in grocery_list:
               all_the_snacks_modified(i, " ")   
#Rewrite your all_the_snacks function so that it takes an additioanl argument called num. Use this variable to customize how many #times your snack is printed out.
def all_the_snacks_modified_again(snack, spacer, num):
           Print((snack + spacer) * num) 
           for i in grocery_list:
               all_the_snacks_modified_again(i, " ", 50)
#Write a price_matcher function that takes no arguments but prints a random item from your grocery list everytime it is run.
import random
def price_matcher():
    grocery_list = ["butter", "bread" "sugar"]
    print(random.choice(grocery_list))
    
#Write an in_grocery_list function that takes a grocery list and prints true if the item is on your grocery list and false if #otherwise
def in_grocery_list(lst):
    '''checks if item is in our grocery list'''
    grocery_list = ["butter", "bread" "sugar"]
for i in list:
    if i in grocery_list:
        print("true")
    else:
        print("false")
basket = ["oil" "ice" "beans"]
in_grocery_list(basket)
#Write the all the snacks function so that num and spacer have default values of 100 and ',' respectively.
def all_the_snacks_modified_twice(snack, spacer=",", num=100):
    print((snack + spacer) * num)
#Challenge: use input to get your neighbors favorite color and store it as a variable.
def get_favorite_color(): 
favorite = input("Enter fav color?: " )
return favorite
print(get_favorite_color())
#Write an april_fools_color_swapper that uses input to get your favorite color, uses input to get your neighbors color and then prints them with your name and your neighbor's name. On the next line, it should swap your color for your neighbors color and print them.
def april_fools_caller_swapper():
    my_name = input("please enter name: ")
    my_favorite_color = input("please enter your favority color: ")
    neighbors_name = input("Please enter you neighbors name: ")
    neighbors_color = input("Please enter your neighbors color: ")
    print(f"My name is {my_name} and my favorite color is {my_favorite_color}, my neighbors name is {neighbor_name} and their favorite color is
          {neighnors_color}")
 
#Create a function called shout which ask a user for their name and shouts it back to them
#So if the use is called Nora, your function should print HELLO NORA!
def shout():
   name = (input("please enter name : ")
   print(f"HELLO {name.upper()}")
shout()






