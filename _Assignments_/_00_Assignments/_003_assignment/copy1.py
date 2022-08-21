import csv
with open("doc.txt",'r') as file:
    read=file.read()
print("input : ",read)
l=read.split(" ")
print(l)
c=0
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in l:
    c=c+1
print(" Count of words :  ",c)
l1=[]
l2=[]
l3=[]
def reverse_fun(word):
    return word[::-1]
for word in l:
    count=0
    for char in word:
        if char in vowels:
            count=count+1
    if count>3:
        l2.append(count)
        revrse_word = reverse_fun(word)
        print("reverse wrd",revrse_word)
        l3.append(revrse_word)
    else:
        l2.append(count)
        l3.append(" ")

    l1.append(word)
    print("count of vowels in word {",word,"} is : ",count)
print("list1: ",l1)
print("list2: ",l2)
print("list3 : ",l3)

def create_list(list1,list2,list3):
    list5=[]
    for i in range(3):
        list5=list(zip(list1,list2,list3))
    print(list5)
    for i in list5:
        #list[i]
        print(list[i])
        print(list5)
    # header=[l1,l2,l3]
    with open('final2.csv', 'w') as f:
        for row in list5:
            for x in row:
                f.write(str(x) + "    ,    ")
            f.write('\n')
    return list5
create_list(l1,l2,l3)
header=[l1,l2,l3]
f=open("csvfile.csv",'w')
writer = csv.writer(f)
# write a row to the csv file
writer.writerow(l1)
writer.writerow(l2)
writer.writerow(l3)
# close the file
f.close()