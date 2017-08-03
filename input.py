'''
#taking input
x = input('Enter name:')
print ('Name',x)
'''

#import module
import statistics

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5] #list

print(statistics.mean(example_list))

from statistics import mean
# so here, we've imported the mean function only.
print(mean(example_list))

# and again we can do as
from statistics import mean as m
print(m(example_list))

from statistics import mean, median
# here we imported 2 functions.
print(median(example_list))


from statistics import mean as m, median as d

print(m(example_list))
print(d(example_list))


from statistics import *

print(mean(example_list))