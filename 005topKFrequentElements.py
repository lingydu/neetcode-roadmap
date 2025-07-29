class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        my_dict={}
        for e in nums:
            if e in my_dict:
                my_dict[e]+=1
            else:
                my_dict[e]=1
        top_k = heapq.nlargest(k,my_dict.items(),key=lambda x:x[1])
        return [item[0] for item in top_k]