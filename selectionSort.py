arr1 = [1,2,7,8,10,10,100]
arr2= [5,6,9,15,20,40,50]
arr3= []

def merge(arr1,arr2,arr3):
    i,j= 0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1

    if i<len(arr1):
        for i in range(i,len(arr1)):
            arr3.append(arr1[i])

    else:
        for i in range(j,len(arr2)):
            arr3.append(arr2[i])
    return arr3
merge(arr1,arr2,arr3)
print(arr3)