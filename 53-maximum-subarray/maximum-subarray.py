class Solution(object):
    def maxSubArray(self, nums):
        maximum,s=min(nums),0
        for x in nums:
            s+=x
            if s<=x:
                s=x
            if s>maximum:
                maximum=s
        return maximum


        