# import pandas as pd
import csv
# import ast
from itertools import zip_longest

with open("doc.txt",'r') as fd:
    file_contents = fd.read()
Reverse_word = []
No_of_vowels_each_word = []
No_of_words = []
for word in file_contents.split():
    count = 0
    No_of_words.append(word)
    for j in word:
        if (j == "a" or j == "e" or j == "i" or j == "o" or j == "u" or j == "A" or
                j == "E" or j == "I" or j == "O" or j == "U"):
            count +=1
    No_of_vowels_each_word.append(count)
    if count > 3:
        Reverse_word.append(word[::-1])
    else:
        Reverse_word.append(" ")

print(No_of_words)
print(No_of_vowels_each_word)
print(Reverse_word)

header = [No_of_words,No_of_vowels_each_word,Reverse_word]
export_data = zip_longest(*header, fillvalue = '')
with open(r'C:\Users\PREETI\PycharmProjects\VN2_T04_226_Core_Python\VN2_T04_Python_Training\_Assignments_\_00_Assignments\_003_assignment\my.csv', 'w') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(('words','vowels','revrse_word'))
      wr.writerows(export_data)
myfile.close()