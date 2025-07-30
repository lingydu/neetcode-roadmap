class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]*len(nums)
        right=[1]*len(nums)
        res=[1]*len(nums)
        i=1
        j=len(nums)-2
        while j>=0:
            right[j]=right[j+1]*nums[j+1]
            j=j-1
        while i<len(nums):
            left[i]=left[i-1]*nums[i-1]
            res[i]=left[i]*right[i]
            i=i+1
        res[0]=left[0]*right[0]
        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        right=1

        for i in range(1,len(nums)):
            res[i]=res[i-1]*nums[i-1]

        for j in range(len(nums)-1,-1,-1):
            res[j]=right*res[j]
            right=right*nums[j]

 
        return res
