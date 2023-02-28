'''
module name: rentv
function name: validate
overview of this function:
1) Customer interaction for what and how much the want to rent.
2) check the user interaction valid or not with exception handelling.
3) calculating the customer renting costume
4) show the last update of the the stocks
5) write the invoice for customer with unique naming
'''

import datetime#importing datetime from python library
import math  #importing datetime from python library
import random#importing random from python library
import convert#importing convert module
import update#importing update module
import Display#importing Display module
import quantityvalidate#importing quantityvalidate module

#creating dictionary and list
bill={"Costume Name ":[],"Brand Name ":[],"Price per piece ":[]}
totalp=[]

def validate():
    """function to rent the costumes by providing the costume id, quantity and costumer name
    and write the bill"""
    
    while(True):
        #Exception handling for costume id 
        success = False
        while success == False:
            try:
                costume_id=int(input("\n\nEnter Id you want to rent: "))
                success=True
            except:
                print("Please enter valid Id")

                
        #Comparing the costume id     
        if costume_id>0 and costume_id<=len(convert.dictionary_costume):
            print("\nThe Custome ID is: ", costume_id)
            print("++++++++++++++++++++++++\nCostume is available\n++++++++++++++++++++++++\n")
            Quantity=quantityvalidate.validate_quantity(convert.dictionary_costume,costume_id)
            select_costume=convert.dictionary_costume[costume_id]


            '''
            In the following operation:
            1) Adding price ,costume name and brand to dictionary whereas prc to list.
            2) Updating the stocks.
            3)Asking user if he want to return more and taking input for his choice.
            ''' 
            if int(select_costume[3])>=Quantity:     
                print("*******************\nQuantity available\n*******************")
                update_qty=int(select_costume[3])-Quantity
                select_costume[3]=str(update_qty)
                price=select_costume[2]
                bill["Price per piece "].append(price)
                prc=float(price.replace("$",""))*Quantity
                totalp.append(prc)
                Costume_name=select_costume[0]
                bill["Costume Name "].append(Costume_name)
                Brand_name=select_costume[1]
                bill["Brand Name "].append(Brand_name)
                print("The price of the custome is:",price)
                update.update_stock()

                print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\
                    \nDo you want to rent another custome as well\n")
                choice=input("Please enter 'y' to rent other clothes else Enter any other variables: ").lower()
                print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                
                if choice=="y":         
                    print("+++++++++++++++++++++++++++++++\nLet's rent a costume\n+++++++++++++++++++++++++++++++")
                    Display.display()
                    validate()
                    '''
                    In the following operation:
                    1) write a each unique invoice name which includes random number and _rent as well.
                    2) write a returned costume name and details in file (invoice).
                    3) write a fine amount and final payable amount in file (invoice).
                    '''            
                else:
                    Total=math.fsum(totalp)
                    name=input("\nEnter name of the customer: ")
                    print("\n********************************************************")
                    print("\n********************************************************")
                    dt=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().hour)+"-"+str(datetime.datetime.now().minute)+"-"+str(datetime.datetime.now().second)
                    t=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day) #date
                    d=str(t)
                    x=str(datetime.datetime.now().day)#date
                    u=str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+":"+str(datetime.datetime.now().second) #time
                    e=str(u)    #time
                    title=str(random.randint(1,100))
                    file=open(title+"rent.txt","w")#generate a unique invoice name and open it in write mode.
                    file.write("Date: "+d)
                    file.write("\t\t\t\tHARRY COSTUME RENTAL")                               
                    file.write("\n=============================================================")
                    file.write("\n\t\t\t\tINVOICE")
                    file.write("\n\nInvoice: "+title)
                    file.write("\n\nName of Customer: "+str(name)+"")
                    file.write("\n=============================================================\n")
                    for key,values in bill.items():#In this loop, write in a file only those costume which is returned by user.
                        file.write('%s:%s\n\n' % (key, ",".join(values)))
                    file.write("Total Price:$"+str(Total))                   
                    file.write("\n********************************************************\n")
                    file.close()
                break

        else:
            print("ERROR!!!\
            \nID entered is out of range")
      

