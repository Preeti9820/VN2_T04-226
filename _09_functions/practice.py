'''
# 1.recursive function
def printUptoN(n):
    if n > 1:
        printUptoN(n - 1)
    print(n, end=" ")

n = int(input("Enter the upper limit="))

printUptoN(n)
'''

# 2.check given word is palindrome or not
'''
def isPalindrome(s):
    return s == s[::-1]
# Driver code
s =input("enter word")
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")
'''
# 3.print even and odd numbers
'''
def num(n):
    if n%2==0:
        print(n,"is even")
    else:
        print("not even")

num(69)

'''
# 4.print prime numbers
'''
def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i / 2) + 1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

starting_range = 2
ending_range = 200
lst = prime(starting_range, ending_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)
    

#5.factorial of given number
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while (n > 1):
            fact *= n
            n -= 1
        return fact
num = 9
print("Factorial of", num, "is",factorial(num))


#6.convert list/tuple/set to list/tuple/set
def convert(x):
    y=set(x)
    print(y)
x=input("enter list")
convert(x)

#7.find cube/square of a number
def math(x):
    y=x*x
    z=x*x*x
    print("squre is:",y,"and cube is:",z)
x=int(input("enter a number"))
math(x)


#8.table of the given number
def table(x):
    for i in range(11):
        z=x*i
        print("The table of",x,"with",i,"is-:",z)
x=int(input("enter a number"))
table(x)


#9.find the Max of three numbers
def max(a,b,c):
    if a>b>c:
        print(a,"is greater")
    elif a<b>c:
        print(b,"is greater")
    else:
        print(c,"is greater")
max(43,22,9)


#10.fibonacci series?
def fibo(x):
    for i in range(x):
        z=i+(i+1)
    print("fibonaci is:",z)
x=int(input("enter number"))
fibo(x)


#11. sum all the numbers in a list
def sum(list):
    z=0
    for i in range(len(list)):
        z+=list[i]
    print("sum of list is ",z)
list=[8,0,7,5,4,8,3,77,543]
sum(list)


#12.multiply all the numbers in a list
def mul(list):
    z=1
    for i in range(len(list)):
        z= z*list[i]
    print("multiplication is",z)
list=[8,7,5,4,8,3,77,543]
mul(list)



#13.to reverse a string
def rev(x):
    print(x[::-1])
x=input("enter your string:")
rev(x)


#14.check whether a number is in a given range
def range_or_not(number,s):
    if s in number:
        print('Number is present in range')
    else:
        print('Number is not present in range')


number = list(input("enter list"))
s = input("number")
range_or_not(number,s)


#15.accepts a string and calculate the number of upper case letters and lower case letters
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')


#16.takes a list and returns a new list with unique elements of the first list.
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x
print(unique_list([1,2,3,3,3,3,4,5]))
'''

#17. 



