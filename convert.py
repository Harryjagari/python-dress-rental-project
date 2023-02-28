'''
Module name:convert
function nmae:conveert_dictionary
overview of this function:
1) Open and read the file New.txt.
2) Convert the lines of file as list and adding in dictionary.
''' 
def convert_dictionary():
    dictionary = {}
    file = open("New.txt","r")#Reading the file
    costume_id = 0
    for line in file:
        costume_id += 1
        line = line.replace("\n","")
        line = line.split(",")#Converting the lines to list
        dictionary[costume_id] = line#Adding the list to dictionary
    file.close()
    return dictionary
dictionary_costume = convert_dictionary()
