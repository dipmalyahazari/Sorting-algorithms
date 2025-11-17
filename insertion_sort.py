def insertionSort(nums):
    for i in range(1,len(nums)):
        key=nums[i]
        j=i
        while j>=1 and nums[j-1]>key:
            nums[j]=nums[j-1]
            j-=1
        nums[j]=key
    return nums

if __name__=='__main__':
    print(insertionSort([12,1,34,2,3,78]))
