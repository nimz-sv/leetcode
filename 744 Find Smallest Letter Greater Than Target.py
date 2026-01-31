class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = -1
        for char in letters:
            if ord(char)>ord(target):
                ans = char
                break
        return ans if ans!= -1 else letters[0]
