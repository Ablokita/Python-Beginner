a = int(input('enter the first number '))
b = int(input('enter the second number '))
x = input('select an operator { + , - , * , /} ')
if x == '+' :
    print(str(a + b))
elif x == '-' :
    print(str(a - b))
elif x == '*' :
    print(str(a * b))
elif x == '/' :
    print(str(int(a / b)))
else :
    print('Invalid input !')
temp = int(input("enter the temptarure : "))
if temp > 30:
    print("It's a hot day")
    print("Drink lots of water")
elif temp > 20:
    print("It's a nice day")
    print("Done !")