class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        d = {}
        output = 0
        for i in range(n): 
            d[(position[i])] = (target-position[i]) / speed[i]
        keys = sorted(position)

        for i in range(n - 1, -1, -1): 
            if d.get(keys[i]): 
                key = keys[i]
                for j in range(i-1, -1, -1): 
                    if (d.get(keys[j]) and d.get(key)):
                        if (d[keys[j]] <= d[key]): 
                            d.pop(keys[j])
        return len(d)



            

         