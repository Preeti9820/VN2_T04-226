import pandas as pd
import csv
import re

class Phone_data():

    def _init_(self):
        self.rows = []
        with open(r"phone_dataset.csv", 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                self.rows.append(row)

    def divide_of_numbers_and_names(self,rows):
        number = []
        personal_data = []
        for i in rows:
            each_data = []
            for j in i:
                if j.isnumeric():
                    number.append(j)
                else:
                    each_data.append(j.strip())
            personal_data.append(each_data)
        return personal_data, number

    def add_to_the_total_data(self,personal_data,number):
        new_num = []
        for n in number:
            new_num.append('(%s) %s-%s' % tuple(re.findall(r'\d{4}$|\d{3}', n)))
        personal_data_1 = personal_data.copy()
        for chr in range(len(personal_data)):
            add_num = ''
            for i in range(len(new_num)):
                if chr == i:
                    add_num += new_num[i]
            personal_data[chr].append(add_num)
        # print(personal_data_1)
        dict = {}
        for chr in personal_data_1:
            dict[chr[0]] = chr
        return dict
    '''
    def result_oftelephone_data(self,personal_data_1):
        dict = {}
        for chr in personal_data_1:
            dict[chr[0]] = chr
        print(dict)
    '''
phone_obj = Phone_data()
x = phone_obj.divide_of_numbers_and_names(phone_obj.rows)
y = phone_obj.add_to_the_total_data(x[0],x[1])
# phone_obj.result_oftelephone_data(phone_obj.add_to_the_total_data(x[0],x[1]))
# print(y)
# print('Result_1:',y['Doe'])
# print('Result_2:',y['John'])
# print('Result_3:',y['Bill'])


read_file = pd.read_csv(r"D:\\Python\VN2 Training\Python\11_File_Handling\_1_search_tele_results\query.txt")
read_file.to_csv(r'D:\\Python\VN2 Training\Python\11_File_Handling\_1_search_tele_results\query.csv', index = None)
res_file = []
with open(r"D:\\Python\VN2 Training\Python\11_File_Handling\_1_search_tele_results\query.csv",'r') as result_file:
    csvreader = csv.reader(result_file)
    for i in csvreader:
        res_file.append(i)
        print(res_file)
        result = 0
        for j in res_file:
            result += 1
            print('Result_' + str(result) + ': ', j[0], ':-', y[j[0]])