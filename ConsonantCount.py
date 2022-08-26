# My solution
def ConsonantCount(strParam):
    # code goes here,
    consonant_number = 0
    strParam=strParam.lower()
    consonant = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
    for i in range(len(strParam)):
        for j in range(len(consonant)):
            if strParam[i]==consonant[j]:
                consonant_number += 1
    return consonant_number
# keep tihs function call here
print(ConsonantCount(input("Write String :")))

# second solution :
def ConsonantCount(strParam):
    # code goes here,
    vowel = ('a','e','ı','i','o','ö','u','ü')
    strParam= strParam.replace(" ", "")
    consonant_number = len(strParam)
    strParam=strParam.lower()
    for i in range(len(strParam)):
        for j in range(len(vowel)):
            if strParam[i] == vowel[j]:
                consonant_number -= 1
    return consonant_number
# keep tihs function call here
print(ConsonantCount(input("Write String :")))


