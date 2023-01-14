import pandas as pd # importing pandas library for handling excel or csv files
import os # importing os module

# scanning folder to get file names and extensions
files = os.listdir("Name Sorter\Assets") # locate files in the Name Sorter/Assets directory

print("These are the files in the Assets folder :")

# dictionary to store files
file_container = {}

for number, file in enumerate(files) : 
    file_container.update({number+1 : file}) # to update the dictionary
    print(f"{number+1}. {file}") # print out files

print("Which file do you want to use?")
selection = int(input("File Number : ")) # input for determining which file wil be used

'''
Function to read a file. Actions are based on the file type.
Parameters :
- file_container : dictionary containing files
- number : integer, input number
Return :
list of names contained in the file
'''
def read_file(file_container=None, number=None) :
    if file_container is None :
        print("No container detected...")
        return
    file_name = file_container[number]
    names = []
    if file_name.endswith(".txt") :
        data = open(fr"Name Sorter\Assets\{file_name}")
        names = data.readlines()
        data.close()
        del names[0]
    elif file_name.endswith(".xlsx") :
        # using pandas to read excel file
        data = pd.read_excel(fr"Name Sorter\Assets\{file_name}")
        names = [name for name in data["Names"]]
    return names

'''
Function to sort names.
Parameters :
- names : list of names from the selected file
Return :
list of sorted names
'''
def sort_names(names) :
    names.sort()
    return names

unsorted_names = read_file(file_container, selection)

print("Unsorted names :") # print unsorted names
for name in unsorted_names :
    print(name)

print("\n")

sorted_names = sort_names(unsorted_names) # print sorted names

print("Sorted names : ")
for name in sorted_names :
    print(name)