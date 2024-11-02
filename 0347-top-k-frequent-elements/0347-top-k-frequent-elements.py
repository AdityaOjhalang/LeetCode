class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        for key,val in counts.items():
            heapq.heappush(heap , (val,key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [val[1] for val in heap]
        
