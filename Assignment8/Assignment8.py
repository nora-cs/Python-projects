#Exercise 1
#go to this website http://www.fullbooks.com/ and copy the text from any of the books and save it to a text file. You should know how to do ths.
#Write a function called file_capitalize that takes two arguments, an input file and an output file. The output file should contain all the text from the input file but all the first letters in the words should be in uppercase.

import sys
def file_capitalize(file_1, file_2):
    '''Takes a file and returns another file with all words capitalized'''
    #open the first file
    with open(file_1, 'r') as opened_file:
         #get contents of the file
         content = opened_file.readlines()
         #Read one line after the other
         for line in content:
             #get each word from the line
             new_line = line.split()
             #use list comprehension to create a new list with capital letters
             new_line = [word.capitalize() for word in new_line]
             #open your new file and write the new lines to  it
             with open(file_2, 'a') as write_file:
                 #put the linens back together
                 print(''.join(new_line), file=write_file)
                 
    #exercise 2
    #Write a function called file_word_count that takes one argument, a file name and returns a dictionary of all 
    #the words in the input file with the number of times each word appears in the dictionary
      #create a function called file_word_count
      #takes one argument which is our imput file
      #returns a dictionary with all the words and thier counts
      
    def file_word_count(file1): #define our function takes one argument
        word_count = dict() #This creates an empty dictionary that will hold our words and thier count
        with open(file1, 'r') as opened_file: #here we open file
            content = opened_file.readlines() #here we create a variable to store contents of file
            for line in content: #we are reading the line from the saved variable
                lst_of_words = line.split() #we are splitting the lines to get each word by itself
                for word in lst_of_words: #we are going to iterate over our list of words
                    word_count[word] = 0 #initialize the word count to zero
                    count = lst_of_words.count(word) #counts a number of times the word appears in a line
                    word_count[word] += count #puts a word in a dict plus its count if it does not already exit
            return word_count #this return statement signifies the end of the line ...or the function
         
            if __name__=="__main__":
                file_capitalize(sys.argv[1], sys.argv[2])
                print(file_word_count(sys.argv[1]))
#call the file using:
#python assignment8/assignment8.py assignment8/twelfth_night.txt assignment8/new_file.txt
             
                
                 
                 
    

