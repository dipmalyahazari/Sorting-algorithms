def selectionSort(nums):
	for i in range(len(nums)):
		min_index=i
		for j in range(i,len(nums)):
			if nums[min_index]>nums[j]:
				min_index=j
		nums[min_index],nums[i]=nums[i],nums[min_index]
	return nums

if __name__=='__main__':
	print(selectionSort([12,1,34,6,56]))
