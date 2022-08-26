"""
ThreeFive Multiples
Have the function ThreeFiveMultiples(num) return the sum of all the multiples of 3 and 5 that are below num. Fow example: if num is 10, the multiples of 3 and 5 that are below 10 are 3,5,6, and 9, and adding them up you get 23, so your program should return 23. The interger being passed will be between 1 and 100.
Examples:
    input: 6
    output: 8 (3,5)

    input: 1
    output: 0
"""
# My solution
def ThreeFiveMultiples(num):
    #code goes here
    sum=0
    for i in range(1,num):
        if i%3==0:
            sum +=i
        elif i%5==0:
            sum += i
    return sum
#keep this function call here
print(ThreeFiveMultiples(int(input("Enter a number: "))))

#second solution :
def ThreeFiveMultiples(num):
    #code goes here
    sum=0
    for i in range(1,num):
        if i%3==0 or i%5==0:
            sum+=i
    return sum
# keep this function call here
print(ThreeFiveMultiples(int(input("Enter a number: "))))

# third solution :
def ThreeFiveMultiples(num):
    #code goes here
    total=0
    total=sum(i if i%3==0 or i%5==0 else 0 for i in range(1,num))
    return total
# keep this function call here
print(ThreeFiveMultiples(int(input("Enter a number: "))))

# fourth solution :
sum=0
def ThreeFiveMultiples(num):
    #code goes here
    i=1
    sum=0
    while(i<num):
        if i%3==0 or i%5==0:
            sum+=i
            i+=1
        else:
            sum += 0
            i += 1
    return sum
# keep this function call here
print(ThreeFiveMultiples(int(input("Enter a number: "))))

