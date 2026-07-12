class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = {}
        output = []
        for i in range(len(points)):
            dist = math.sqrt(points[i][0] * points[i][0] + points[i][1] * points[i][1])
            if not d.get(dist): 
                d[dist] = []
            d[dist].append(points[i])
        keys = sorted(d.keys())
        i = 0
        count = 0
        while count < k: 
            count += len(d[keys[i]])
            output += d[keys[i]]
            i += 1

        return output
        