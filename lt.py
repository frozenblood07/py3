#list and tuples

#tuple -> immutable
def example():
    return 15, 12

x, y = example()
print(x,y)
# in the above case, we have used a tuple and cannot modify it... and
# we definitely do not want to!

#list is array -> mutable
x = [1,3,5,6,2,1,6]

'''
You can then reference the whole list like:
'''
print(x)

# or a single element by giving its index value.
# index values start at 0 and go up by 1 each time

print(x[0],x[1])



# first we need an example list:
x = [1,6,3,2,6,1,2,6,7]
# lets add something.
# we can do .append, which will add something to the end of the list, like:
x.append(55)
print(x)

#will insert 33 at 2 index
x.insert(2,33)
print(x)

#will remove the first occurance of 6
x.remove(6)
print(x)

print(x[5])

#will get the index at which 1 is present
print(x.index(6))

#count the occurances of 1 in the list
print(x.count(1))

#length of x
print(len(x))

#sort
x.sort()
print(x)

y = ['Jan','Dan','Bob','Alice','Jon','Jack']
y.sort() #sort asc
print(y)
y.reverse() #sort desc
print(y)

#multi dimentional lists
x = [[2,6],[6,2],[8,2],[5,12]]
print(x[2])

print(x[2][1])


y = [[5,2],
     [6,2],
     [3,1],
     [12,6]
    ]

print(y)