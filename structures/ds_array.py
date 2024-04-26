#!/usr/bin

from array import array

def print_array(arr:array):
    for x in range(len(arr)):
        print(arr[x],end=",")
    print("")

arr = array ('i',[1,23])
print_array(arr)
arr.append(10)
print_array(arr)
print(arr.index(10))
print_array(arr)
arr.pop()
print_array(arr)
arr.pop(5)
print_array(arr)

