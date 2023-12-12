def findsmall(arr):
    smallest = arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index

def sort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest=findsmall(arr)
        newArr.append(arr.pop(smallest))
    return newArr

c=sort([5,3,4,9,1])
print(c)