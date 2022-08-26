"""
Have the function CheckNums(num1,num2) take both paramaters being passed and return the string
true if num2 is greater than num1,
otherwise return string false.
If the parameter values are equal to each other then return the string -1.

Examples:
    input : 3 & num2=122
    output : true

    input : 67 & num2=67
    output : -1
"""
#My solution :
def CheckNums(num1,num2):
    #code goes here,
    if num2>num1:
        return "true"
    elif num1>num2:
        return "false"
    else:
        return "-1"
#keep this function call here
print(CheckNums(int(input("First Num :")),int(input("Second Num :"))))

