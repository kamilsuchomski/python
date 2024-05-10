import random
import math
import sys
from timeit import default_timer as timer



A = []

#function for initiating list with random numbers
def initA(arr, n):
    #for other numbers randoming option comment two below lines and...
    numbers = list(range(0, n))
    random.shuffle(numbers)
    
    for i in range(n):
        #arr.append(random.randint(0, 100000))
        #...uncomment line above and comment line below
        arr.append(numbers[i])
        
        
        
#quickSort implementation with partition function        
def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)
        
        
    
#partition implementation with pivot setted at last element of list 
def partition(A, p, r):
    pivot = A[r]
    smaller = p
    
    for i in range(p ,r):
        if A[i] <= pivot:
            A[smaller], A[i] = A[i], A[smaller]
            smaller += 1
    
    A[smaller], A[r] = A[r], A[smaller]
    
    return smaller



#quickSort implementation with partitionMiddle function        
def quickSortM(A, p, r):
    if p < r:
        q = partitionMiddle(A, p, r)
        quickSortM(A, p, q - 1)
        quickSortM(A, q + 1, r)
        
        
        
#partition implementation with pivot setted at middle element of list 
def partitionMiddle(A, p, r):       
    A[(p + r) // 2], A[r] = A[r], A[(p + r) // 2]
    pivot = A[r]
    smaller = p
        
    for i in range(p, r):
        if A[i] <= pivot:
            A[smaller], A[i] = A[i], A[smaller]
            smaller += 1
    
    A[smaller], A[r] = A[r], A[smaller]
    
    return smaller



###
#changing recursion limit for testing functions with higher numbers
sys.setrecursionlimit(20001)

nn = [100, 500, 1000, 5000, 7500]

for n in nn:
    initA(A, n)
    
    B = A.copy()
    
    
    
    #quickSort with pivot setted at last element of list
    
    start = timer()
    quickSort(A, 0, len(A) - 1)
    stop = timer()
    #time for unsorted array
    t1 = stop - start
    
    start = timer()
    quickSort(A, 0, len(A) - 1)
    stop = timer()
    #time for sorted array
    t2 = stop - start
    
    #quickSort n= n, unsorted, sorted
    print("quickSort  n=", n, t1, t2)
    
    
    
    #quickSort with pivot setted at middle element of list
    
    start = timer()
    quickSortM(B, 0, len(B) - 1)
    stop = timer()
    #time for unsorted array
    t3 = stop - start
    
    start = timer()
    quickSortM(B, 0, len(B) - 1)
    stop = timer()
    #time for sorted array
    t4 = stop - start
    
    #quickSortM n= n, unsorted, sorted
    print("quickSortM n=", n, t3, t4, "\n")