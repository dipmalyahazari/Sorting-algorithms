def bubbleSort(nums):
    for i in range(len(nums)-1):
        flag=True
        for j in range(i,len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                flag=False
        if flag:
            break
    return nums
if __name__=='__main__':
    print(bubbleSort([9,1,23,4,56]))
