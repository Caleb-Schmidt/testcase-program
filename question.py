# Given an array nums, write a function to move all 
# zeroes to the end of it while maintaining the relative order of
# the non-zero elements.
array1 = [0, 1, 0, 3, 12]
# Output:
# [1, 3, 12, 0, 0]

array2 = [1, 7, 0, 0, 0, 8, 0, 10, 12, 0, 4]
# Output:
# [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]

def zeros(alist):
    for item in alist:
        if item == 0:
            alist.append(alist.pop(alist.index(0)))
    return alist

print(zeros([1,2,3,4,5]))