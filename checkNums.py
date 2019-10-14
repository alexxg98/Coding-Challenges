# Solution to 'Check Nums' Challenge using Java
#
# Have the function CheckNums(num1,num2) take both parameters being passed and return the string true if num2 is greater than num1, otherwise return the string false. If the parameter values are equal to each other then return the string -1.

def checkNums(num1, num2):
    """Check if num1 is less than num2"""
    if(num1<num2):
        return "true"
    elif(num1>num2):
        return "false"
    else:
        return "-1"

print("Check Nums Challenge")
input1 = int(input("Enter num1: "))
input2 = int(input("Enter num2: "))
print("Is num1 less than num2? ==> ", checkNums(input1, input2))
