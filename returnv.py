'''
module name: returnv
function name: returned
overview of this function:
1) Customer interaction for what and how much he want to return.
2) check the user interaction valid or not with exception handelling.
3) calculating the customer returning costume
4) show the last update of the the stocks
5) write the invoice for customer with unique naming
'''

import datetime#importing datetime from python library
import math    #importing datetime from python library
import random   #importing random from python library
import convert  #importing convert module
import update  #importing update module
import Display#importing Display module
import quantityvalidate#importing quantityvalidate module


#creating dictionary and list
bill_return={"Costume Name ":[],"Brand Name ":[],"Price per piece ":[]}
totalp=[]
totalF=[]

def returned():
    """function to return the costumes by providing the bill number costume id, quantity and costumer name
    which automatically comparares the returning day and generates fine and write the bill"""
    while(True):
        #Exception handling for bill number
        loop=False
        while loop==False: 
            try:
                bill_no=int(input("Please enter your bill no.: "))
                B=open(str(bill_no)+"rent.txt","r")
                print("=====================\nBill matched\n=====================")
                loop=True
            except:
                print("=====================\nBill no. did not match\n=====================")
                
        #Exception handling for costume id         
        success = False
        while success == False:
            try:
                costume_id=int(input("\n\nEnter Id you want to return: "))
                success=True
            except:
                print("***********************\nPlease enter valid Id\n***********************")

        #Comparing the costume id   
        if costume_id>0 and costume_id<=len(convert.dictionary_costume):
            print("\nThe Custome ID is: ", costume_id)
            print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nCostume Id that you want to return is matched\
                    \n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            Quantity=quantityvalidate.validate_quantity(convert.dictionary_costume,costume_id)
            select_costume=convert.dictionary_costume[costume_id]
            
            '''
            In the following operation:
            1) Adding price ,costume name and brand to dictionary whereas prc to list.
            2) Updating the stocks.
            '''   
            print("***********************\nReturned Successfully\n***********************")
            update_qty=int(select_costume[3])+Quantity
            select_costume[3]=str(update_qty)
            price=select_costume[2]
            bill_return["Price per piece "].append(price)
            prc=float(price.replace("$",""))*Quantity
            totalp.append(prc)
            Costume_name=select_costume[0]
            bill_return["Costume Name "].append(Costume_name)
            Brand_name=select_costume[1]
            bill_return["Brand Name "].append(Brand_name)
            print("\nThe price of one custome is:",price)
            update.update_stock()
            
            '''
            In the following operation:
            1) Reading 14 characters of the file for the date.
            2) Only date is extracted by replacing other string with "".
            '''     
            content=B.read(15)
            print("Rented",content)
            C=content.replace("Date: ","")
            e=str(C)
            t=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day) #date
            d=str(t)
            
            '''
            In the following operation:
            1) Changing the format and returning the value as string representation of date.
            2) Comparing the rented date and todays date and calculate the days for late returning.
            3)Asking user if he want to return more and taking input for his choice.
            '''   
            d1 = datetime.datetime.strptime(e, "%Y-%m-%d")
            d2 = datetime.datetime.strptime(d, "%Y-%m-%d")
            total=0
            if d2>d1:
                delta = d2 - d1
                D=str(delta)
                D=D.replace("days, 0:00:00","")
                day=str(D)
                days=int(day)
                if int(days)>5:
                    total=days-5
                    Fine=total*Quantity*7
                    totalF.append(Fine)
                    print("You are "+str(total)+" days late")
            else:
                total=0
                    

            print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\
                    \nDo you want to return another custome as well\n")
            choice=input("Please enter 'y' to return other clothes else Enter any other variables: ").lower()
            print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                
            if choice=="y":        
                print("Let's return a costume\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                Display.display()
                returned()
                '''
                In the following operation:
                1) write a each unique invoice name which includes random number and _return as well.
                2) write a returned costume name and details in file (invoice).
                3) write a fine amount and final payable amount in file (invoice).
                '''
            
            else:
                Totalfine=math.fsum(totalF)
                if  total>0:
                    print("You have returned these costumes "+str(total)+" days late"+"\nSo, your total fine amount is $"+str(Totalfine))
                else:
                    print("You are on time")
                Total=math.fsum(totalp)
                Totalamount=float(Totalfine)+float(Total)
                name=input("\nEnter name of the customer: ")
                print("\n********************************************************")
                print("\n********************************************************\n")
                title=str(random.randint(1,100))
                dt=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().hour)+"-"+str(datetime.datetime.now().minute)+"-"+str(datetime.datetime.now().second)#date
                u=str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+":"+str(datetime.datetime.now().second) #time
                e=str(u)
                file=open(title+"return.txt","w")#generate a unique invoice name and open it in write mode.
                file.write("Date: "+d)
                file.write("\t\t\t\tCOSTUME RENTAL") 
                file.write("\n=============================================================")
                file.write("\n\t\t\t\tINVOICE")
                file.write("\n\nInvoice: "+title)
                file.write("\n\nName of Customer: "+str(name)+"")
                file.write("\n=============================================================\n")
                for key,values in bill_return.items():#In this loop, write in a file only those costume which is returned by user.
                    file.write('%s:%s\n\n' % (key, ",".join(values)))
                file.write("Fine Amount:$"+str(Totalfine))
                file.write("\n\nTotal Price:$"+str(Totalamount))
                file.write("\n********************************************************\n")
                file.close()
            break

        else:
            print("ERROR!!!\
            \nID entered is out of range")
        
       

    
    
    
        
