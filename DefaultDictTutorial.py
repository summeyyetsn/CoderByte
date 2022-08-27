"""
DefaultDict Tutorial
In this challenge, you will be given  integers,  and .
There are  words, which might repeat, in word group .
There are  words belonging to word group . For each  words,
check whether the word has appeared in group  or not.
Print the indices of each occurrence of  in group .
If it does not appear, print -1.

STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b

Sample Output
1 2 4
3 5
"""
my_dict={}
list_a=list()
a,b = input().split()
a=int(a)
b=int(b)
for x in range(a):
    item=input()
    list_a.append(item)
my_dict["A"]=list_a
item=""
list_b=list()
for y in range(b):
    item=input()
    list_b.append(item)
my_dict["B"]=list_b
for i in range (len(list_b)):
    result = list()
    my_str=""
    for j in range(len(list_a)):
        if list_b[i] in list_a[j]:
            result.append(j+1)
    if not result:
        result.append(-1)
    for item in result:my_str += str(item)+" "
    print(my_str)


