'''1) Sum
of
elements
list = [45,78,5,19,3,7]
print("sum of list: ",sum(list))
'''
# 2) Mulitply of elements
'''list = [ 1,2,3,4]
print(list * 3)'''
'''
# 3) Largest number from list

largest = [2, 5, 9, 0, 2, 6, 7, 14, 15, 20]
print("largest number in the list", max(largest))

    ( or)
largest = [2, 5, 9, 0, 2, 6, 7, 14, 15, 20]
large = max(largest)
print("the largest numberis :", large)

4)Smallest
number
from list

smallest = [110,2.25,156,16.9]
print("the smallest number is :", min(smallest))

5)   count
no
of
strings
whose
length is 2
a = ['Ananaya', 'An', 'yht', 'jk']
b = ['waer', 'shfdijs', 'bh', 'hg']
List = []
for i in a:
    if
len(i) == 2:
List.append(i)
print(List)
list_2 = []
for i in b:
    if
len(i) == 2:
list_2.append(i)
print(list_2)
print(List + list_2)

7) Remove
duplicates
a = [1, 2, 3, 3, 3, 34, 4, 4, 45]
b = set(a)
print(b)

# 8) Check list is empty or not
a = []
if not a:
    print("the list is empty")
else:
    print("not empty")

    (OR)

a = []
if len(a) == 0:
    print("list is empty")
else:
    print("not empty")

#9) Clone or copy
num = [5, 23, 6, 12, 45]
num1 = num.copy()
print(" print the new list num1", num1)

# 11) Find common element from 2 lists
cabin1 = ["Ananya", "Anusha", "Jashuva", "Preeti", "Adithi"]
cabin2 = ["Adithi", "Rahul", "Preeti", "Ananya", "Anusha"]
s1 = set(cabin1)
s2 = set(cabin2)
s3 = s1.intersection(s2)
common = list(s3)
print(common)
'''
'''
12) Remove
specified
index
from list and print

c = ['a', 'g', 'y', 'rr']
c.remove('rr')
print(c)
'''




