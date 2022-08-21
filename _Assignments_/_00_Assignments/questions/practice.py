'''
try:
    f=lambda x:x*x
    value=f(5)
    print("value=",value)
except Exception :
    print("error occur")
finally:
    print("its done.")
'''

'''
class A:
    def cat(self):
        print("its a cat function")
    def dog(self):
        print("its a dog function")
class B(A):
    def animal(self):
        print("its a animal function")
    def all(self):
        print("its a all function.")
x=B()
x.cat()




import csv
vc=0
cc=0
s="preeti priyanka"
x=['a','e','i','o','u']
str=s.lower()
for i in range(0,len(str)):
    if str[i] in x:
        vc+=1
    else:
        cc+=1
print(vc)
print(cc)
fname="preetii.csv"
fields=['col1','col2']
with open(fname,'w') as csvfile:
    write=csv.writer(csvfile)
    write.writerow([vc,cc])


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)
'''





'''
file=open("preeti.txt",'w')
file.write("preeti,VN2-226,banglore")
file.close()
'''


def dec(fun):
    def add():
        fun()
        x="preeti"
        y=x.upper()
        print("Upper value is:",y)

    return add()
@dec
def fun():
    print("second")


