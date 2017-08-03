print('Single Quotes')
print("double quotes")
print('can do this',5) # , will add a space between this and 5. + will not add a space.
#print('cannot do this:'+5) #can't add  concatenate a string and integer in py
#print('Can't do this')
print('you\'ll have success here')
print("you'll have success here too")


#while loop
condition = 1 #variable
while condition < 10:
    print(condition)
    condition += 1

#for loop
list = [1,2,3,4,5,6,7,8]

for x in list:
    print (x)


for x in range(1,11):
    print (x)


#if else elif statement
x = 10
y = 15
z = 22
if x > y :
    print ('success')
elif x < z:
    print ('elif')
else :
    print ("else")


#functions
def example(x,y=100):
    z = x +y
    print (z)

example(x,y)
example(x)
