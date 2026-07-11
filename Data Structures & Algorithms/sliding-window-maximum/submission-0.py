class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        
        for i in range(len(nums)-k+1):
            a=nums[i]
            for j in range(i,i+k):
                a=max(a,nums[j])
            res.append(a)
        return res
