print("------------capitalize----------")
msg = "preeti priyanka"
msg.capitalize()      #without variable it autommatically goes to garbage.
print(msg)
print("msg=",msg.capitalize())
msg1=msg.capitalize()
print("msg=",msg1)


print("--------------center(width, fillchar)-------------------------")
msg="preetipriyanka"
print(msg.center(30,'t'))


print("-----------------count(str, beg= 0,end=len(string))----------------")
msg="preetipriyanka"
print(msg.count('p'))


print("----------------decode(encoding='UTF-8',errors='strict')-----------------")
msg="preeti priyanka"
x=msg.encode('UTF-8','strict')
print(x)
print(msg.decode('UTF-8','strict'))


print("--------------endswith(suffix, beg=0, end=len(string))------------------")
msg="preeti priyanka"
print(msg.endswith('a',2,17))


print("---------------expandtabs(tabsize=8)--------------------")
msg = "preeti priyanka"
print(msg.expandtabs())


print("---------------find(str, beg=0 end=len(string))--------------------")
msg = "preeti priyanka"
print(msg.find('i', 3 ,9))


print("---------------index(str, beg=0, end=len(string))--------------------")
msg = "preeti priyanka"
print(msg.find('y', 3 ,15))



print("---------------isalnum()--------------------")
msg = "preeti8@ priyanka"
print(msg.isalnum())



print("---------------join(seq)--------------------")
msg = "preeti8@ priyanka"
print(msg.join(msg))


print("---------------len(string)--------------------")
msg = "preeti8@ priyanka"
print(len(msg))



print("---------------ljust(width[, fillchar])--------------------")
msg = "preeti8@ priyanka"
print(msg.ljust(30,'*'))



print("---------------lower()--------------------")
msg = "PREETI PRIYANKA"
print(msg.lower())



print("---------------lstrip()--------------------")
msg = "         PREETI PRIYANKA"
print(msg.lstrip())



print("---------------lstrip()--------------------")
msg = "         PREETI PRIYANKA"
print(msg.lstrip())