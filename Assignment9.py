#Create a list with 5 file names.
import os
file_names = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"]
# Write a function to create folder and then create the five 5 files in the previous exercise into it.
folder = 'Assignment_folder'
#Your function should write the name of the file as the contents of the file.Refer to slack for correct code for this section!
def create_folder(folder_name, file_names):
    """creates a folder and writes some files into it"""
    os.mkdir(folder_name)#makes a new folder!
    os.chdir(new_folder)#changes into the folder we just created
    for file in file_names:#we iterate through the provided list of files
        with open(file, 'w') as a_file:#we open each file as a_file, =touch in linux
            print(file, file=a_file)#we write to it, and we write by writing its name
    os.chdir('..')
    print('I am done creating all files.')#if you want to be fancy.


#Write some code to read the files that you just created in the previous exercise
def read_files(folder_name):#read files in a directory and splits the lines into the component
    for root, subs, files in os.walk(folder_name):#we iterate through the provided dir or folder
        for file in files:#we focus only on the files in the dir
            with open(file, 'r') as a_file:#we open each file in read mode
                lines = a_file.readlines()#we grab all the lines in the file
                for line in lines:#then we iterate over all the lines
                    for i in line.split():#we split each line
                    print(i)#we print the contents from the split
    print('I am done with reading all the files in the directory')

if __name__=="__main__":
    create_folder(folder, file_names)
