class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = []
        d = {}
        for i in range(n): 
            d[(position[i])] = (target-position[i]) / speed[i]
        positions = sorted(position)
        output = 0
        for i in range(n): 
            # print(positions[i], speed[i], (target-positions[i]) / speed[i])
            stack.append(d[positions[i]])

        while stack: 
            e = stack.pop()
            output += 1
            # print("e", e)
            while stack and  e >= stack[-1]: 
                # print(stack[-1])
                stack.pop()
            
        return output



            

         