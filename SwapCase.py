"""
Swap Case
Have the function SwapCase(str) take the str parameter and swap the case of each character. For example: if str is "Hello World" the output should be hELLO wORLD. Let number and symbols stay the way thet are.
Examples:
    input : "Hello-LOL"
    output : hELLO-lol

    input : "Sup DUDE!!?"
    output : sUP dude!!?
"""
def SwapCase(str):
    # code goes here,
    new_str=""
    for i in range(len(str)):
        if str[i].islower():
            new_str+=str[i].upper()
        elif str[i].isupper():
            new_str+= str[i].lower()
        else:
            new_str += str[i]
    return new_str
# keep this function call here
print(SwapCase(input("Enter the String : ")))

# second solution :
def SwapCase(str):
    # code goes here,
    new_str=''
    for char in str:
        if char.isupper():
            lower = char.lower()
            new_str += lower
        else:
            upper = char.upper()
            new_str += upper
    return new_str
# keep this function call here
print(SwapCase(input("Enter the String : ")))