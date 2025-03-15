numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers.append(6) #adds a new value at the end of the list
print(numbers)
numbers.insert(0, -1) #inserts a new value at the given position in the list
print(numbers)
numbers.remove(3) #removes the value given in the function from the list, not the value at the index number
print(numbers)
print(2 in numbers) # searches for the given value in the list and returns a boolean value
print(3 in numbers) # returns false
print(len(numbers)) #returns the number of elements in a list
print('for loop')
for i in numbers:
    print(i)
print('while loop')
i=0
while i<len(numbers):
    print(numbers[i])
    i+=1
numbers.clear() #empties the list
print(numbers)