"""
Pentagonal Number
Have the function PentagonalNumber(num) read num which will be a positive integer
and determine how many dots exist in a pentagonal shape arounda a center dot on the Nth iteration.
For example, first iteration there is only one single dot,
on the second iteration there are 6 dots,
on the third there are 16 dots,
and on the fourth there are 31 dots.
Examples:
    1. iteration : 1 dot
    2. iteration : 6 dots
    3. iteration : 16 dots
    4. iteration : 31 dots
    5. iteration : 51 dots

    (1) , (1+5) , (1+5+10) + (1+5+10+15) .....
    1+5(1+2+3+4+5....)
"""
def PentagonalNumber(num):
    #code goes here,
    dot=1
    for i in range(1,num):
        dot += i*5
    return dot
#keep this function call here
print(PentagonalNumber(int(input("Enter the number of iterations: "))))

# second solution :
#1+5(1+2+3+4+5....)
def PentagonalNumber(num):
    #code goes here,
    dot=1
    for i in range(num):
        dot+=5*(i)
    return dot
#keep this function call here
print(PentagonalNumber(int(input("Enter the number of iterations: "))))

# thirt solution :
def PentagonalNumber(num):
    #code goes here,
    return 1+sum(i*5 for i in range(1,num))
# keep this function call here
print(PentagonalNumber(int(input("Enter the number of iterations: "))))

# fourth solution :
def PentagonalNumber(num):
    #code goes here,
    if num==1:
        return 1
    else:
        return ((num-1)*5) + PentagonalNumber(num-1)
# keep this function call here
print(PentagonalNumber(int(input("Enter the number of iterations: "))))
