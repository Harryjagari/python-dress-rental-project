'''
Module name:main
function nmae:function
overview of this function:
1) Print the options to choose.
2) As per user requirement run the program
by calling the appropriate function of appropriate module.
''' 
import Display#importing Display module
import rentv#importing rentv module
import returnv#importing returnv module
def function():
    print("++++++++++++++++++++++++++++++++++++++\
    \nWelcome to costume rental Application\
    \n++++++++++++++++++++++++++++++++++++++\n")
    while(True):    
        print("Select your desirable option\
        \n(1) || press 1 for view a costume\
        \n(2) || Press 2 for renting a costume.\
        \n(3) || Press 3 for returning a costume.\
        \n(4) || Press 4 to exit from the application.\n")
        #exception handling for the options
        try:
            choose=int(input("Enter your option: "))
            if choose==1:
                print("\nThese are the Costumes available\n")
                Display.display()#Calling the display function of Display module
        
            elif choose==2:
                print("\nLet's rent a costume\n")
                Display.display()#Calling the display function of Display module
                rentv.validate()#Calling the validate function of rentv module
            elif choose== 3:
                print("\nLet's return a costume.\n")
                Display.display()#Calling the display function of Display module
                returnv.returned()#Calling the returned function of returnv module
            elif choose== 4:
                print("\nThank you for using our Application.\n")
                break
            else:
                print("Invalid input!!!!\
                \nPlease Select the value as per the provided option.\n")
        except:
            print("Please enter the valid costume ID")
function()
