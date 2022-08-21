print("---------------first 10 natural number------------------")
n=1
while n <= 10 :
    print(n)
    n += 1
print("-----------END------------")


print("-----------Pattern------------")
n=5
for i in range (1,n+1,1):
    for j in range (1,i+1):
        print(j, end=' ')
    print(" ")
print("-----------END------------")

'''print("-----------Pattern------------")
n=5
for i in range (1,n+1):
    for j in range (1,i+1):
        print(i, end=' ')
    print(" ")
print("-----------END------------")


print("-----------Multiple------------")
num = int(input("enter the Number"))
for i in range (1,11):
    mul=i*num
    print("the multiplication of ",i,"*",num,"=",mul)'''


'''num= int(input("number"))
if num%6==0:
    print("number is diveisble by 6")
elif num%3==0:
    print("number is diveisble by 3")
elif num%2==0:
    print("number is diveisble by 2")
else:
    print("number is not diveisble by 6,2,3")  '''

count = ''
for i in range(10,21):
    for j in range(2,i):
        if i%j ==0:
            break
    else:
        print(i)


'''
num=int(input("number"))
x = 2
while num>x:
    if num% x ==0 :
        x += 1
    else:
        pass
if x >1:
    print("No Prime number")
else:
    print("Prime number")
'''


