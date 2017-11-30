#/usr/bin/python

colors = ['red', 'blue', 'green']
squares = [1, 4, 9, 16, 25, 36, 49, 64]
primes = [2, 3, 5, 7, 11]
grades = [64, 100, 89, 78, 92]
animals = ('cat', 'dog', 'lion', 'tiger', 'bear')

#group 1
#print(colors)

#colors.append('purple')
#print(colors)

#printing this returns None, but still alters the list
#print(colors.append('orange'))

#colors.insert(2, 'pink')
#print(colors)

#group 2
#print("Before:")
#print(squares)
#print(primes)
#squares.extend(primes)
#print("After:")
#print(squares)
#print(primes)

#group 3
#print("Before:")
#print(squares)
#squares.remove(16)
#print("After:")
#print(squares)

#returns ERROR
#primes.remove(24)

#group 4
#print(primes)
#print(primes.index(7))
#print(primes.index(17))

#group 5
#print("Before:")
#print(grades)
#print(colors)
#grades.sort()
#colors.reverse()
#print("After:")
#print(grades)
#print(colors)

#group 6
#print(squares)
#popped = squares.pop(3)
#print(popped)
#print(squares)

#group 7
#print(primes)
#print(colors)
#myList = primes + colors * 2
#print(myList)

#group 8
#colors.extend(['orange', 'teal', 'pink', 'purple'])
#print(primes)
#print(primes[3:])
#print(colors)
#print(colors[2:6])
#print(colors[2])
#print(squares)
#print(squares[:-4 : 2])

#group 9
#print(colors)
#colors[2] = 'teal'
#print(colors)
#colors[2:3] = "teal"
#print(colors)
#colors[2:3] = ["teal", "indigo"]
#print(colors)
#colors[2:3] = ["teal", "indigo", "violet"]
#print(colors)

#group 10
#print(animals)
#animals.append('giraffe')
#animals.remove('bear')
#print(animals[3])
#lAnimals = list(animals)
#lAnimals.insert(2, 'fox')
#print(lAnimals)

#group 11
#print(animals)
#print(len(animals))
#print(squares)
#print(len(squares))
