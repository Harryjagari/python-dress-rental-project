'''
Module name:Display
function nmae:display
overview of this function:
1) Open and read the file New.txt.
2) print the line of text file.
''' 
import convert#importing the convert module
def display():
    count=0
    print("-"*80)
    print("ID \t Custome Name \t\t\tBrand Name\tprice\tQuantity")
    print("-"*80)
    file=open("New.txt","r")#Reading the text file
    counter = 0
    for line in file:
        counter += 1
        line = line.replace(",","\t")
        print(counter,"\t" ,line)#printing the counter and lines
    file.close()

