arr = [8,5,7,3,4,6,1,2]
def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    print(left,right)
    return merge(mergeSort(left),mergeSort(right))
    



def merge(left,right):
    arr3 =[]
    i,j= 0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr3.append(left[i])
            i+=1
        else:
            arr3.append(right[j])
            j+=1

    if i<len(left):
        for i in range(i,len(left)):
            arr3.append(left[i])

    else:
        for i in range(j,len(right)):
            arr3.append(right[i])
    return arr3

print(mergeSort(arr))

