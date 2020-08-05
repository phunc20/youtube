'''
Here we sort the arrays to ascending order;
descending order can be done similarly.

The idea behind bubble sort is
    Keep iterating thru the array and swapping neighboring elements
    until an iteration in which no swap takes place, then we know
    the array is sorted.

Author: phunc20
'''
import time

def em_bubble_sort(arr):
    while True:
        corrected = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                corrected = True
        if not corrected:
            # Then the arr must be sorted because
            # arr[i] <= arr[i+1] for all i.
            return arr

def same2_but_diff(arr):
    while True:
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            # Then the arr must be sorted because
            # arr[i] > arr[i+1] never takes place.
            return arr

def test(arr, impl):
    original_arr = arr.copy()
    sorted_ = sorted(arr)
    start = time.time()
    if impl(arr) == sorted_:
        end = time.time()
        print("{}: Suceeded. Took {}s".format(original_arr, end-start))
    else:
        print("{}: Failed. Becomes {}".format(original_arr, arr))



print("em_bubble_sort")
print("-------------------------------------")
### Example taking 1 iteration (an already-sorted array): O(n)
##print(em_bubble_sort([1,2,3,4,5,6]))
#test([1,2,3,4,5,6], em_bubble_sort)
### Example taking 2 iterations
##print(em_bubble_sort([1,3,2,4,5,6]))
#test([1,3,2,4,5,6], em_bubble_sort)
### average O(n^2)
##print(em_bubble_sort([4,2,3,1,6,5]))
#test([4,2,3,1,6,5], em_bubble_sort)
### worst O(n^2)
##print(em_bubble_sort([6,5,4,3,2,1]))
#test([6,5,4,3,2,1], em_bubble_sort)
for arr in [[1,2,3,4,5,6],
            [1,3,2,4,5,6],
            [4,2,3,1,6,5],
            [6,5,4,3,2,1],]:
    test(arr, em_bubble_sort)


print(end="\n")
print("same2_but_diff")
print("N.B. This is a wrong implementation.\n`for-else` is to be used along w/ `break`, not like this")
print("-------------------------------------")
for arr in [[1,2,3,4,5,6],
            [1,3,2,4,5,6],
            [4,2,3,1,6,5],
            [6,5,4,3,2,1],]:
    test(arr, same2_but_diff)


'''
-------------
  Analysis
-------------
def em_bubble_sort(arr):
    while True:                                                c1       x
        corrected = False                                      c2       x
        for i in range(0, len(arr) - 1):                       c3       (n-1)*x
            if arr[i] > arr[i+1]:                              c4       (n-1)*x
                arr[i], arr[i+1] = arr[i+1], arr[i]            c5       (n-1)*x
                corrected = True                               c6       (n-1)*x
        if not corrected:                                      c7       x
            # Then the arr must be sorted because               0
            # arr[i] > arr[i+1] never takes place.              0
            return arr                                         c8       1

If the smallest element is at the last entry, we see that in this case x is at least n-1.
Therefore, we see that the worst case, if exists, is at least O(n^2).


'''
