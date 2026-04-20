class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDictSet = set(wordDict)
        n = len(s)
        curr = []
        result = []
        def backtracking(index):
            if index == n:
                result.append(" ".join(curr))
            # base case
            for i in range(index, n):
                word = s[index: i + 1]
                if word in wordDictSet:
                    curr.append(word)
                    backtracking(i + 1)
                    curr.pop()

        backtracking(0)
        return result
            



        