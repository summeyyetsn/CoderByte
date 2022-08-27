"""
Prime Time
Have the function PrimeTime(num) take the num parameter being passed
and return the string true if the parameter is a prime number,
otherwse return the string false.
The range will be between 1 and 2^16.
Examples:
    input : 19
    output : true

    input : 110
    output : false
"""
# My solution :
def PrimeTime(num):
    # code goes here,
    flag=False

    if num == 1 : flag = True
    elif num == 2 : flag = False
    for i in range(3,num):
        if num % i == 0:
            flag=True
    if flag==True: message="false"
    else: message="true"
    return message
# keep this function call here
print(PrimeTime(int(input("Enter a numb: "))))

#second solution :
