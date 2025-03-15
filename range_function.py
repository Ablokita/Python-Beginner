#it is used to generate a sequence of numbers
numbers = range(5) #numbers is a list of numbers from 0 to 5, excluding 5
print(numbers)
for n in numbers:
    print(n)
nu = range(5, 10) # a sequnce of numbers from 5 to 10 excluding 10
print('\n')
for i in nu:
    print(i)
print('\n')
sequence = range(5, 10, 2) #prints a sequence of numbers incrementd by 2 from 5 to 10
for s in sequence:
    print(s)
print('\n')
for x in range(5): #traversing a sequence without storing it in a variable
    print(x)