"""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

"""
#
# Read this data from a text file and find
# 1. No.of words
# 2. No.of vowels in each word
# 3. If there are more than 3 vowels in a word, reverse that word
# Finally, store the data into CSV file
# The first column of CSV file will be a word
# The second column will be No of vowels
# The third Column will be if a word has more than 3 vowels reverse the string

# import panda as pd
# import csv

# my_file=open("docfile.docx",'r')
# file=my_file.read()
vowels=0
words=0
dict={}
# lines=file.split('.')
v_list=['a','e','i','o','u','A','E','I','O','U']
with open('doc.txt','r') as file:
    content=file.read()
    word=content.split(" ")
    # print(word)
    print(len(word))
    c=0
    for i in word:
        final = [each for each in i if each in v_list]
        dict[c] = len(final)
        c += 1
    print(dict)
    for i in dict.keys():
       # print(dict[i])
        if dict[i] > 3:
            print(i)
