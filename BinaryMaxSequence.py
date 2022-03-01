import math
import os
import random
import re
import sys

def to_bytes(theInt):
    a = [1]
    numtot = 0
    num = 1
    while numtot<1000000:
        num*=2
        numtot+=num
        a.append(num)
        
    a.reverse()
    for k, v in enumerate(a):
        if theInt-v>=0:
            theInt=theInt-v
            a[k]=1
        else:
            a[k]=0
            
    return a
    
def max_in_array(theArray):
    theMax = 0
    for v in theArray:
        if v>theMax:
            theMax = v
    return theMax

def byte_max_seq(bitArray):
    maxseq = [0] * len(bitArray)
    maxind = 0
    for k,v in enumerate(bitArray):
        if v==0:
            maxind+=1
        else:
            maxseq[maxind]+=1
    return max_in_array(maxseq)

if __name__ == '__main__':
    n = int(input().strip())
    m = to_bytes(n)
    print(byte_max_seq(m))
