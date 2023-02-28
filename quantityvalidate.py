'''
module name: quantityvalidate
function name: validate_quantity
overview of this function:
1) check the user interaction valid or not with exception handelling.
'''
def validate_quantity(dictionary,costumeID):
    success = False
    while success == False:
        try:
            quantity = int(input("Enter the Quantity: "))#Input for quantity
            while quantity<=0 or quantity>int(dictionary[costumeID][3]):
                print("Please enter valid input")
                quantity = int(input("Enter the Quantity: "))#Input for quantity
            success = True
        except:
            print("Invalid input has been provided")
    return quantity


