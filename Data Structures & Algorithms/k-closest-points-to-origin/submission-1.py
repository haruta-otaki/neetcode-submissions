class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i in range(len(points)): 
            d = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            if len(max_heap) < k: 
                heapq.heappush(max_heap,[-d, points[i]])
            else: 
                if -max_heap[0][0] > d: 
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, [-d, points[i]])
        output = []
        for e in max_heap: 
            output.append(e[1])
        return output
        