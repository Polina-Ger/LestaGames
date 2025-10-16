import random

def sorting (arr):
    length=len(arr)
    for i in range(length-1):
        index_min=i
        for j in range(i+1, length):
            if arr[index_min]>arr[j]:
                index_min=j
        if index_min!=i:
            arr[i],arr[index_min]=arr[index_min],arr[i]

arr = arr2 = [random.randint(0, 100) for _ in range(1000)]
sorting(arr)

def quicksort(arr):
    if len(arr)<=1:return arr
    left=[]
    right=[]
    middle=[]
    pivot = arr[len(arr)//2]
    for i in range(len(arr)):
        if arr[i]<pivot:
            left.append(arr[i])
        elif arr[i]>pivot:
            right.append(arr[i])
        else: middle.append(arr[i])
    return quicksort(left)+middle+quicksort(right) 

a = quicksort(arr2)