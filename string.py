#reverse string and remove duplicates

def swap(s,i,j):
    lst = list(s);
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

def strRevDup(string):
    keyDict = {}
    strLen = len(string)
    left = 0
    right = strLen-1
    lu = 0
    ru = 0

    while left < right:
        cl = string[left]
        cr = string[right]
        print(cl,cr,'cjar')

        #character didn't repeat yet
        if cl not in keyDict or lu == 1:
            keyDict[cl] = 1
            lu = 1
        else:
            left += 1

        if cr not in keyDict or ru == 1:
            keyDict[cr] = 1
            ru = 1
        else:
            right -= 1


        if lu == 1 and ru == 1:
            print(lu, ru, keyDict,left,right)
            string = swap(string, left, right)
            left += 1
            right -= 1
            lu = 0
            ru = 0
        '''  
        elif lu == 0:
            string = string[:lu] + string[lu + 1:]
        elif ru == 0:
            string = string[:ru] + string[ru + 1:]
        '''




    return string


string = 'aabbbcd'

string = strRevDup(string)
print('string is',string)