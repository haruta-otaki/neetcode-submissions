class Solution:
    def isPalindrome(self, s: str) -> bool:
        # put 2 pointers at the start back; check whether the same until it switches index 
        # clean  loops through every character and keeps it only if it is alphanumeric 
        string = ""
        for ch in s: 
            if (ch.isalnum()): 
                string += ch.lower()
        j = 0 
        k = len(string) - 1
        for i in range(len(string) // 2): 
            if j > k: 
                break
            if (string[j] != string[k]): 
                return False
            j += 1
            k -= 1
        return True