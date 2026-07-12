class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=[]
        counts=[]
        for num in nums:
            if num not in l:
                l.append(num)
        for num in l:
            cnt=0
            for x in nums:
                if x==num:
                    cnt+=1
            counts.append((cnt, num))
        counts.sort(reverse=True)
        res = [x[1] for x in counts[:k]]
        return res