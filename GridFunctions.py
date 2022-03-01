import math
import os
import random
import re
import sys

def print_grid(array2d):
    for _ in array2d:
        row = ""
        for v in _:
            row += str(v)+" "
        print(row)
        
def array_sum(array2d):
    theSum = 0
    for d in array2d:
        for e in d:
            theSum += e
    return theSum
    
def array_mult(first2d, second2d):
    arrayReturn = first2d
    for k,v in enumerate(first2d):
        for d,e in enumerate(v):
            arrayReturn[k][d] = e * second2d[k][d]
    return arrayReturn

def array_sect(array2d,x,y,w,h):
    newArray = [[0] * w for i in range(h)]
    for k,v in enumerate(array2d, start = y):
        if k>=y+h:
            break
        for d,e in enumerate(v, start = x):
            if d>=x+w:
                break
            newArray[k-y][d-x] = array2d[k][d]
    return newArray
    
def grab_grids(array2d, w, h):
    arrw = len(array2d[0])
    arrh = len(array2d)
    most = 0
    for i in range(arrh-h+1):
        for j in range(arrw-w+1):
            partGrid = array_sect(array2d,j,i,w,h)
            newGrid = array_mult(partGrid,hourglass)
            print_grid(newGrid)
            total = array_sum(newGrid)
            if total>most:
                most = total
            print(array_sum(newGrid))
            print(" ")
    return most

if __name__ == '__main__':

    arr = []
    hourglass = [[1, 1, 1],[0, 1, 0],[1, 1, 1]]
    
    for _ in range(6):
        wop=[]
        for v in range(6):
            wop.append(random.randint(0,9))
        arr.append(wop)
        
    print_grid(arr)
    print(" ")
    portionArray = array_sect(arr,2,0,3,3)
    print_grid(portionArray)
    print(" ")
    multGrid = array_mult(portionArray,hourglass)
    print_grid(multGrid)
    print(" ")
    print(array_sum(multGrid))
    print(" ")
    print(grab_grids(arr,3,3))
