'''
Module name:update
function nmae:update_stock
overview of this function:
1) Open and write the file New.txt.
2) Update the stocks.
''' 
import convert
def update_stock():
    f=open("New.txt","w")#opening the file in write mode
    for key,values in convert.dictionary_costume.items():
        f.write(",".join(values))#writing in file
        f.write("\n")
    f.close()#closing file
