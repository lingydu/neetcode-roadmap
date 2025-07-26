class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict={}
        for i, e in enumerate(nums):
            compl=target-e
            if compl in myDict:
                return [myDict[compl],i]
            myDict[e]=i
