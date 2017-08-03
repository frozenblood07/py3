exNum1 = -5
exNum2 = 5
print(abs(exNum1))
if abs(exNum1) == exNum2:
    print('True!')

import time
# will work in a typical installation of Python, but not in the embedded editor
help(time)

#find max and min in list
exList = [5,2,1,6,7]

largest = max(exList)
print(largest)

smallest = min(exList)
print(smallest)

#rounding up
x = 5.622
x = round(x)
print(x)

y = 5.256
y = round(y)
print(y)


#str to int
intMe = '55'
intMe = int(intMe)
print(intMe)


#int to str
stringMe = 55
stringMe = str(stringMe)
print(stringMe)

#int to float
floatMe = 55
floatMe = float(floatMe)
print(floatMe)