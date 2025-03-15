wt = float(input('Weight: '))
unit = input('(K)g or (L)lb: ')
if (unit == 'K') or (unit == 'k'):
    print('Weight in Pounds: '+str(w / 0.45359237))
elif (unit =='L') or (unit =='l'):
    print('Weight in Kg: '+str(w * 0.45359237))
else:
    print('invalid input')