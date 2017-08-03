
#find element in unsorted array
def findElmentUnsorted(arr, n, key):
    for i in range(n):
        if (arr[i] == key):
            return i

    return -1


arr = [12, 34, 10, 6, 40]
key = 40
n = len(arr)

# search operation
index = findElmentUnsorted(arr, n, key)
if index != -1:
    print("element found at position: " + str(index + 1))
else:
    print("element not found")


#insert
arr.append(55)
print(arr)

#will insert 33 at 2 index
arr.insert(2,33)
print(arr)

#will remove the first occurance of 6
arr.remove(6)
print(arr)


#binary search
def binarySearch(arr,key,start,end):
    if(start > end):
        return -1

    mid = int((start+end)/2)
    if(arr[mid] == key):
        return mid

    if(arr[mid] > key):
        return binarySearch(arr,key,start,mid-1)
    else:
        return binarySearch(arr,key,mid+1,end)


arrSorted = [1,2,3,4,5,6,7,8,9,10,11,13]
index = binarySearch(arrSorted,1,0,len(arrSorted) -1)
print ('index is', index)

#insert into sorted array
import bisect
bisect.insort(arrSorted,12)
print (arrSorted)

arrSorted.remove(11)
print(arrSorted)

for i in range(len(arrSorted)):
    print (arrSorted[i])

#reverse array recursive
def arrReverse(arr,start,end):
    if(start > end):
        return;

    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp

    arrReverse(arr,start+1,end-1)


arrReverse(arrSorted,0,len(arrSorted)-1)
print(arrSorted)


#print leader in array
def arrLeader(arr,arrLen):
    max = arr[arrLen-1]
    print (max)
    for i in range(arrLen-2,0,-1):
        if(arr[i] > max):
            print (arr[i])
            max = arr[i]

arr = [16, 17, 4, 3, 5, 2]
arrLeader(arr,len(arr))

# Python program to find if there are two elements wtih given sum
CONST_MAX = 100


# function to check for the given sum in the array
def printPairs(arr, arr_size, sum):
    # initialize hash map as 0
    binmap = [0] * CONST_MAX

    for i in range(0, arr_size):
        temp = sum - arr[i]
        if (temp >= 0 and binmap[temp] == 1):
            print ("Pair with the given sum is", arr[i], "and", temp)
        binmap[arr[i]] = 1
        #print (binmap)

# driver program to check the above function
A = [1, 4, 45, 6, 10, -8]
n = 16
printPairs(A, len(A), n)


# Program for finding out majority element in an array

# Function to find the candidate for Majority
def findCandidate(A):
    maj_index = 0
    count = 1
    for i in range(len(A)):
        if A[maj_index] == A[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count = 1
    return A[maj_index]


# Function to check if the candidate occurs more than n/2 times
def isMajority(A, cand):
    count = 0
    for i in range(len(A)):
        if A[i] == cand:
            count += 1
    if count > len(A) / 2:
        return True
    else:
        return False


# Function to print Majority Element
def printMajority(A):
    # Find the candidate for Majority
    cand = findCandidate(A)

    # Print the candidate if it is Majority
    if isMajority(A, cand) == True:
        print(cand)
    else:
        print("No Majority Element")


# Driver program to test above functions
A = [2, 2, 2, 3, 3,1,2]
printMajority(A)


# Python program to find the element occurring odd number of times

def getOddOccurrence(arr):
    # Initialize result
    res = 0

    # Traverse the array
    for element in arr:
        # XOR with the result
        res = res ^ element
    return res


# Test array
arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]

print ("%d" % getOddOccurrence(arr))


# Python program to find maximum contiguous subarray

# Function to find the maximum contiguous subarray
def maxSubArraySum(arr,arrLen):
    max_till_now = 0
    max_ending_here = 0

    for i in range(arrLen-1):
        max_ending_here += arr[i]

        if(max_ending_here < 0):
            max_ending_here = 0
        elif(max_ending_here > max_till_now):
            max_till_now = max_ending_here

    print ('Max Sum',max_till_now)

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
maxSubArraySum(arr,len(arr))


# getMissingNo takes list as argument
def getMissingNo(A):
    n = len(A)
    total = int((n + 1) * (n + 2) / 2)
    sum_of_A = sum(A)
    return total - sum_of_A


# Driver program to test above function
A = [1, 2, 4, 5, 6]
miss = getMissingNo(A)
print('Missing number',miss)

#Search an element in sorted and rotated unique array using
#single pass of Binary Search

def searchSPA(arr,low,high,key):
    if(low > high):
        return -1
    mid = int((low+high)/2)
    print(mid,'mid')

    if(arr[mid] == key):
        return mid

    #if first half of the array is sorted
    if(arr[low] <= arr[mid]):
        if(key >= arr[low] and key <= arr[mid-1]):
            return searchSPA(arr,low,mid-1,key)

        return searchSPA(arr,mid+1,high,key)
    #second half must be sorted
    else:
        if(key >=arr[mid+1] and key <=arr[high]):
            return searchSPA(arr,mid+1,high,key)


    return searchSPA(arr,low,mid-1,key)


arr = [8,9,10,11,1,2,3,4,5,6,7]
index = searchSPA(arr,0,len(arr)-1,11)

print("index is",index)


def moveToEnd(arr,arrLen):
    pos = arrLen - 1
    for i in reversed(range(arrLen)):
        print(i,arr[i])
        if(arr[i] != 0):
            arr[pos] = arr[i]
            pos -= 1
    return arr

#Merge an array of size n into another array of size m+n
def merge(mPlusN,N,n,m):
    i=n
    j= 0
    k=0
    while k < (m + n):
        ''' Take an element from mPlusN[] if
           a) value of the picked element is smaller and we have
              not reached end of it
           b) We have reached end of N[] '''
        if ((i < (m + n) and mPlusN[i] <= N[j]) or (j == n)):
            mPlusN[k] = mPlusN[i]
            k += 1
            i += 1
        else:  # Otherwise take element from N[]
            mPlusN[k] = N[j]
            k +=1
            j +=1
    return mPlusN


arrMplusN = [2, 8, 0, 0, 0, 13, 0, 15, 20]
arrN = [5, 7, 9, 25]

arrMplusN = moveToEnd(arrMplusN,len(arrMplusN))
arrMplusN = merge(arrMplusN,arrN,len(arrN), len(arrMplusN) - len(arrN))
print('m+n',arrMplusN)


def reverseArr(arr,start,end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
    return arr

def leftrotate(arr,arrLen,d):
    arr = reverseArr(arr,0,d-1)
    arr = reverseArr(arr,d, arrLen -1)
    arr = reverseArr(arr,0,arrLen -1)

    return arr

arr = [1,2,3,4,5,6,7]
d = 3

arr = leftrotate(arr,len(arr),d)
print('Left rotate',arr)


# Function to return max sum such that
# no two elements are adjacent
def find_max_sum(arr):
    incl = 0
    excl = 0

    for i in arr:
        # Current max excluding i (No ternary in
        # Python)
        new_excl = excl if excl > incl else incl

        # Current max including i
        incl = excl + i
        excl = new_excl

    # return max of incl and excl
    return (excl if excl > incl else incl)


# Driver program to test above function
arr = [5, 5, 10, 100, 10, 5]
print (find_max_sum(arr))


#quick sort
#swap positions in array
def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def quickSort(arr,low,high):
    if(low >= high):
        return
    left = low
    right = high
    pivot = arr[int((low+high)/2)]
    pos = 0
    while(left <= right):

        while(arr[left] < pivot):
            left += 1
        while(arr[right] > pivot):
            right -= 1

        if(left <= right):
            swap(arr,left,right)
            left += 1
            right -= 1

        print(pos,"swapped arr is",arr)
        pos += 1

    quickSort(arr,low,right)
    quickSort(arr,left,high)




#arr = [1,12,5,26,7,14,3,7,2]
arr = [1, 2, 5, 6, 2]
quickSort(arr,0,len(arr)-1)
print('final quick sort arr',arr)


# Function for nth fibonacci number - Space Optimisataion
# Taking 1st two fibonacci numbers as 0 and 1

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
            print(c)
        return b


# Driver Program

print(fibonacci(9),'fibo')

