class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_cnt, start, max_ones=0, 0, 0
        end=0
        for end in range(len(nums)):
            if nums[end]==0:
                zero_cnt+=1
            while zero_cnt>k:
                if nums[start]==0:
                    zero_cnt-=1
                start+=1
            max_ones=max(max_ones, end-start+1)
        return max_ones