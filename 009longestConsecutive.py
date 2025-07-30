class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        totalset=set(nums)
        longest=0
        for e in totalset:
            if (e-1) not in totalset:
                current=e
                counter=1
                while (current+1) in totalset:
                    counter+=1
                    current=current+1
                longest=max(counter,longest)
        return longest


