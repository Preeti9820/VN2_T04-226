#Length of string
'''
list=[1,2,3,"preeti",(3,7),9]
x=len(list)
print(len(list))
print("Length=",x)
'''

#Count characters in string
'''
list = [1,2,3,"preeti",(3,7),9]
count=0
for i in list:
    count+=1
print(count)
'''

#String slicing
'''
list = [1,2,3,"preeti",(3,7),9]
x=list[3:7]
print(x)
'''

#Length of longest string in python
'''str1 = "preeti"
str2="priyanka"
if len(str1)>len(str2):
    print(str1)
else:
    print(str2)
'''

#First last chars swapping
'''str="preeti"
str2=str[-1]+str[1:-1]+str[0]
print(str2)
'''

#Remove odd index values
'''str="preeti"
result=""
for i in range(len(str)):
    if i%2==0:
        pass
    else:
        result = result + str[i]
print(result)
'''


#Count words in a string
'''str="preeti priyanka"
print(len(str.split()))
'''

#Upper lower case of a string
'''str="preeti priyanka"
print(str.capitalize())
'''


#Last part of string
'''str="preeti priyanka"
words=str.split()
print(words[-1])'''

#Convert a given string to all uppercase
'''str="preeti priyanka"
print(str.upper())'''

#program to remove a newline in Python
'''str="preeti priyanka\n pattnaik"
print(str.replace('\n', ''))'''

#program to check whether a string starts with specified characters
'''str="preeti priyanka"
print(str.startswith('p'))
'''


#to set the indentation of the first line
'''str="preeti"
for t in str:
    print("true")
'''


#to print the following floating numbers upto 2 decimal places
'''a_float = 3.14159
formatted_float = "{:.2f}".format(a_float)
print(formatted_float)
'''


#print the following floating numbers upto 2 decimal places with a sign
'''a = 3.14159
print('%.2f'%a)
'''


#to display a number with a comma separator
'''str="696853265789654125639"
print(str.replace('',','))
'''


#to format a number with a percentage
'''a_number = 54862.896547
percentage = "{:.2%}".format(a_number)
print(percentage)
'''


#to count occurrences of a substring in a string
'''str1 = "This dress looks good you have good taste in clothes."
substr = "good"
count1 = str1.count(substr)
print(count1)
'''


#print the index of the character in a string
'''str="This dress looks good you have good taste in clothes."
for i in range(len(str)):
    print(i)
'''



#convert a string in a list
'''str="This dress looks good you have good taste in clothes."
print(list(str))
'''



#swap comma and dot in a string
'''str="This dress looks good, you have good, taste in clothes,"
print(str.replace(',','@'))
'''


#count and display the vowels of a given text
'''str="This dress looks good, you have good, taste in clothes"
vowels=0
for i in str:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print(vowels)
'''


#remove spaces from a given string
'''str="This dress looks good, you have good, taste in clothes"
print(str.replace(" ",""))
'''


#move spaces to the front of a given string



#capitalize first and last letters of each word of a given string
'''Str = input('Enter the String :')
Str = Str[0:1].upper() + Str[1:len(Str)-1] + Str[len(Str)-1:len(Str)].upper()

print(Str)
'''

#remove duplicate characters of a given string




#Reverse a given string  Input : "Python"   Output : "nohtyP"
'''str="Python"[::-1]
print(str)
'''


#Reverse each word in given string Input
'''str = input('add yours')
print ("The original string  is : ",str)
reverse_String = ""
count = len(str)
while count > 0:
    reverse_String += str[ count - 1 ]
    count = count - 1
print ("The reversed string using a while loop is : ",reverse_String)
'''

#Reverse each word and reverse word again. Input
'''str_2 = "find the first non-repeating character in given string"
str_3 = ""
for i in str_2.split():
    str_3 = str_3 + i[::-1] + " "
print(str_3)
'''

#that accepts a string and calculate the number of digits and letters
'''str = input("Input a string: ")
d=l=0
for i in str:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)
'''



#lowercase first n characters in a string
'''str = 'PREETIPRIYANKA'
print(str[:6].lower() + str[6:])
'''

#split a string on the last occurrence of the delimiter
'''str1 = "gfg, is, good, better, and best"

# printing original string
print("The original string : " , str(str1))

# using rsplit()
# Split on last occurrence of delimiter
res = str1.rsplit(', ', 1)

# print result
print("The splitted list at the last comma : " , str(res))
'''


#find the first non-repeating character in given string








