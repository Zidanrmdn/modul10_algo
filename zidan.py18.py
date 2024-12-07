# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 10:42:39 2024

@author: ASUS
"""

def bubbleSort(array):
    n = len(array)
 
    for i in range(n):
 
        for j in range(0, n-i-1):
 
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
                
def binarySearch(array, l, r, x):
 
    # Check base case
    if r >= l:
 
        mid = l + (r - l) // 2
 
        if array[mid] == x:
            return mid
 
        elif array[mid] > x:
            return binarySearch(array, l, mid-1, x)
 
        else:
            return binarySearch(array, mid + 1, r, x)
 
    else:
        return -1

array = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
x = input("masukan angka: ")
x = int(x)

bubbleSort(array)

result = binarySearch(array, 0, len(array)-1, x)
result = int(result)
print("Tablenya :", array)


if result != -1:
    print("Targetnya ada, di ", (result)+1)
else:
    print("Tidak ada target")
    