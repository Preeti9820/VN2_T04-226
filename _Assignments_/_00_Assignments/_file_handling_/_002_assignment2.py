# .  Create a Multilevel dictionary by reading the provided logfile (PFA) and output the dictionary as
# {"Pattern1":{"line1":"Services","line2":"0001","line3":{"include":"BFE"},"line4":{"Include":"1*1"},
#              "line5":"0","line7":{"Include":"2*2"},"line8":{"services":["stop","pause","delete","startup"]}},
#             "Pattern2":{"line1":"Registry"......}, "Pattern3":{"line1":"Files"......} }

# file=open("logfile.txt",'r')
# d={}
# for line in file:
#     (key, val) = line.split()
#     d[int(key)] = val
# print(d)
# import cvc
dictionary = {}
with open("logfile.txt") as file:
    for line in file:
        (key, value) = line.split("\n")

        dictionary[str(key)] = value

print(dictionary)