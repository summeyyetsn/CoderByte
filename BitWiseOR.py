"""Bitwise One
    Have the function BitwiseONe(strArr) take the array of strings stored in strArr,
    which will only contain two strings of equal length that represent binary numbers,
    and return a final binary string that performed the bitwise OR operation on both strings.
    A bitwise Or operation places a 0 in the new string where there are zeroes in both binary strings,
    otherwise it places a 1 in taht spot.
    For example: if strArr is ["1001","0100"] then your program should return the string "1101"

        Examples:

       input: ["100","000"]
       output: 100

       input: ["00011","01010"]
       output: 01011"""


# My solution :
def BitwiseOne(strArr):
    # code goes here
    my_output = ""
    for i in range(len(strArr[0])):
        if strArr[0][i] == "1" or strArr[1][i] == "1":
            my_output += "1"
        else:
            my_output += "0"

    return my_output


# keep this function call here
print(BitwiseOne(["00011", "01010"]))


# second solution :
# what is zip() function ?
# returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together,
# and then the second item in each passed iterator are paired together etc.
# example:
# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")
# c = ("Ahmet", "Mehmet", "Ali")
# x = zip(a, b, c)
# #use the tuple() function to display a readable version of the result:
# print(tuple(x))
# output: --> (('John', 'Jenny', 'Ahmet'), ('Charles', 'Christy', 'Mehmet'), ('Mike', 'Monica', 'Ali'))

def BitwiseOne(strArr):
    # code goes here
    first, second = strArr[0], strArr[1]
    result = ""
    for a, b in zip(first, second):
        if a == b:
            result += a
        else:
            result += "1"
    return result


# keep this function call here
print(BitwiseOne(["00011", "01010"]))


# third solution :
# What is the join() function?
# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.
# Example:
# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)
# print(x)
# output: John#Peter#Vicky

def BitwiseOne(strArr):
    # code goes here
    result = "".join("1" if i == "1" or j == "1" else "0" for i, j in zip(strArr[0], strArr[1]))
    return result


# keep this function call here
print(BitwiseOne(["00011", "01010"]))

