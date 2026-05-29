class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = min(nums)
        p = max(nums)
        n = abs(p - l)
        print(n + 1)
        c = [0] * (n + 1)
        output = []
        for i in range(len(nums)):
            print (nums[i] - l)
            c[nums[i] - l] += 1

        for i in range(k):
            e = max(c)
            i = c.index(e)
            print("i", i)
            print("actual i", i + l)
            c[i] = 0
            output.append(i + l)

        return output

