a = 10
if a == 10:
    print("Welcome to Hello World")
    print("Welcome again")
print("-----End of if-----")

# Static initialization
x = 10
print("Value of x1: ", x, type(x))

# Dynamic initialization
# x = input()
x = input("Enter value2 : ")  # 100 ==> "100"
print("Value of x2: ", x, type(x))

x = int(input("Enter value3 : "))  # 10 ==> "10" --> 10
print("Value of x3: ", x, type(x))

x = float(input("Enter value3 : "))  # 10.5 ==> "10.5" --> 10.5
print("Value of x3: ", x, type(x))