"""
Two Sum
Have the function TwoSum(arr) take the array of integers stored in arr,
and determine if any two numbers (excluding the first element) in the array can sum up to the first element in the array.
For example: if arr is [7,3,5,2,-4,8,11], then there are actually two pairs that sum to the number 7:
[5,2] an [-4,11].
Your program should return all pairs, with the numbers separated by a comma, in the order the first number appears in the array.
Pairs should be separated by a space.
Do for the example above, your program would return 5,2 and -4,11
If there are no two numbers that sum to the first element in the array, return -1
Examples:
    input : [17,4,5,6,10,11,4,-3,-5,3,15,2,7]
    output : 6,11   10,7    15,2

    input : [7,6,4,1,7,-2,3,12]
    output : 6,1    4,3
"""
#My Solution :
def TwoSum(arr):
    #code goes here,
    key_num = arr[0]
    start = 1
    sum = 0
    couples=()
    for first in range(start,len(arr)):
        for second in range(start+1,len(arr)):
            sum = arr[first] + arr[second]
            if sum == key_num:
                couples = couples + (arr[first],)
                couples = couples + (arr[second],)
            else:
                sum = 0
    for i in range(round(len(couples)/2)):
        print ("".join(f"{couples[i]},{couples[i+1]}"))
#keep this function call here
my_arr=[]
dimension = int(input("Enter array dimension : "))
for j in range(dimension):
    my_arr.insert(j,int(input(f"{j}. element : ")))
print(TwoSum(my_arr))