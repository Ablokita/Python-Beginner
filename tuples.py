# tuples are like lists i.e. they are used to store objects but they are immutable, which means we can't change its values once it is created
numbers = (1, 2, 3, 3, 4, 3) # [] is used to define a list and () is used to define a tuple
print(numbers.count(3)) #returns the number of times 3 appears in the tuple
print(numbers.index(3)) #returns the index of the first occurance of 3