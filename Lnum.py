import numpy as nm

arr = nm.array([1, 2, 3, 4, 5])
print(arr)
print(nm.where(arr==3))
print(type(arr))
print(arr.dtype)

def bn(n,array):

    s =0
    e = array.size -1

    while(s<=e):
        mid = s + (e-s)//2
        if(array[mid]==n):
            return mid
        elif(array[mid]<n):
            s = mid+1
        else: e = mid -1    

    return -1

print(bn(1, arr))    