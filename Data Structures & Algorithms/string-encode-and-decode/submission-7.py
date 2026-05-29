class Solution:

    def encode(self, strs: List[str]) -> str:
        if (not strs): 
            return "*"
        output = ""
        for s in strs:
            output += s + "."

        return output[:len(output)-1]

    def decode(self, s: str) -> List[str]:
        if (s == "*"): 
            return []
        return s.split(".")

