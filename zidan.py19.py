# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 12:32:33 2024

@author: ASUS
"""

def bubble_sort(arr):
  n = len(arr)

  for i in range(n):

    for j in range(0, n-i-1):

      if arr[j] > arr[j+1] :
        arr[j], arr[j+1] = arr[j+1], arr[j]

# Contoh penggunaan
data = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
print("List Sebelum Disorting:")
print(data)

bubble_sort(data)

print("List Yang Sudah Disorting:")
print(data)
