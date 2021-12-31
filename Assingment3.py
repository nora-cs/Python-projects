#write some code that randomly picks a price from your price list (9.42, 5.67, 3.25, 13.40, 7.50) and prints True if the price is greater than 10 or false if its not.
list = [9.42, 5.67, 3.25, 13.40, 7.50]
import random
print(random.choice(list))
5.67
 if price < 10:
    print(False)
else:
    print(True)
    False

#You are provided with the following list ['bread', 'butter', 'groundnuts', 'sugar', 'garri', 'egusi', 'ogboono', 'eru']. Write code to print True if the following item#s ['bread', 'rice', 'okra', 'water', 'egusi'] are found in the list. Can you do this with a for loop?
list =  ['bread', 'butter', 'groundnuts', 'sugar', 'garri', 'egusi', 'og
             boono', 'eru']

exists = True
   for item in list:
if item == 'bread':
   exists = True
      break
   print(True)

#Write a for loop that prints every letter in the phrase "Blood-oxygenation level dependent functional magnetic resource imaging"
phrase  = "Blood-oxygenation level dependent functional magnetic resource imaging"
   for i in phrase:
    print(i)

#Create a grocery list. Now use a for loop to print the words "Note to self, buy" and the grocery item.
grocery_list = [ "lettuce", "carrots", "greens", "bacon"]
    for i in grocery_list:
        print("Note to self, buy", i)

#Now create a for loop that prints a numbered list of your grocery items.
grocery_list = [ "lettuce", "carrots", "greens", "bacon"]
   print(list(enumerate(grocery_list, start=1)))
[(1, 'lettuce'), (2, 'carrots'), (3, 'greens'), (4, 'bacon')]

#Evidently your favorite snack is more important than anything else in your grocery list. Modify the last exercise to stop if and when it finds your favorite snack in y#our grocery list.
for i in grocery_list:
         print(i)
if i == "greens":
         break
#Use the string split method, to segment all the words in the phrase ""Blood-oxygenation level dependent functional magnetic resource imaging" using a for loop.

phrase: "Blood-oxygenation level dependent functional magnetic resource imaging"
i = phrase.split()
    print(i)
 ['Blood-oxygenation', 'level', 'dependent', 'functional', 'magnetic', 'resource', 'imaging']

#Use the range method to write a for loop to print out a numbered grocery list. if you have not created a groucery list, create it.

#Use enumerate to print out a numbered grocery list. if you don't have a grocery list, create one.i
grocery_list = [ "lettuce", "carrots", "greens", "bacon"]
for i, item in enumerate(grocery_list, 1):
        print(i, '. ' + item, sep='',end='')

