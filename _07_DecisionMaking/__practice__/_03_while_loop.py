'''num=int(input("Enter the number"))
mul=1
for i in range(1,num+1):
    mul=mul*i
    print("multiplication is",mul)670
    i +=1
'''

num=int(input("Number:"))

if num > 2000 :
    z=int(num/2000)
    num= num%2000
    print("there are", z, "number of 2000/-")
if num>= 500:
    m=int(num/500)
    num= num%500
    print("there are", m, "number of 500/-")
if num>=100:
    n=int(num/100)
    num= num%100
    print("there are", n, "number of 100/-")
if num>=50:
    o=int(num/50)
    print("there are", o, "number of 50/-")
    num= num%50
if num>=10:
    p=int(num/10)
    num=num%10
    print("there are", p,"number of 10/-")
if num>1:
    q=int(num/1)
    num=num%1
    print("there are", q,"number of 1/-")