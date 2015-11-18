
#Loops

print range(100)
print range(1, 100)

help(range)

for i in range(2, 100, 2): #The first value is where it starts, then where it stops, and finally the increment
	print i

#Tuples -- non-scalar data type, can hold many items

tuples_of_numbers = (3.2, 2, 1, -100, 100, 240)
tuples_of_strings = ('What', 'is', 'a', 'tuple')

print tuples_of_numbers[0]
print tuples_of_strings[-1]
# print tuples_of_strings[4] #Going to give an error, out of range	

print len(tuples_of_strings)

#Immutable data types -- Can't change it!

# tuples_of_numbers[0] = 3 #first element is an example of a element within an immutable data type
# Tuples and strings are both immutable
