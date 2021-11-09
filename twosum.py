nums = [2,7,11,15,1,2,8,5,11]
nums.sort()
target=18
start = 0
end = len(nums)-1
while(start<=end):
    if nums[start]+nums[end] == target:
        print(start,end)
        break
    elif nums[start]+nums[end] < target:
        start+=1

    else: end-=1
    
print(nums)
