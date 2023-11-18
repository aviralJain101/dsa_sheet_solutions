from typing import *

count = 0

def merge(a, l, m, r):
    global count
    n1 = m-l+1
    n2 = r-m
    i = j = 0
    k = l
    a1 = a[l:m+1]
    a2 = a[m+1:r+1]
    while i < n1 and j < n2:
        if a1[i] <= a2[j]:
            a[k] = a1[i]
            i += 1
        else:
            a[k] = a2[j]
            j += 1
            count += (n1 - i)
        k += 1
    while i < n1:
        a[k] = a1[i]
        i += 1
        k += 1
    while j < n2:
        a[k] = a2[j]
        j += 1
        k += 1


def merge_sort(a, l, r):
    if l >= r:
        return
    m = (r-l)//2 + l
    merge_sort(a, l, m)
    merge_sort(a, m+1, r)
    merge(a, l, m, r)


def numberOfInversions(a : List[int], n : int) -> int:
    # Write your code here.
    global count
    count = 0
    merge_sort(a, 0, n-1)
    return count
    
