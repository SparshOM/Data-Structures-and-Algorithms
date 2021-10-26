arr = [10,3,1,9,4,18,5]
swapped= True
i=0
while swapped:
    swapped= False
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            swapped=True
print(arr)
