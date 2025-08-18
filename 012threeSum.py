class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        ans=[]
        for i,e in enumerate(nums):
            if i>0 and nums[i-1]==e:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                
                if e+nums[left]+nums[right]<0:
                    left+=1
                elif e+nums[left]+nums[right]>0:
                    right-=1

                else:
                    ans.append([e,nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right -=1
                    left+=1
                    right -=1
        return ans