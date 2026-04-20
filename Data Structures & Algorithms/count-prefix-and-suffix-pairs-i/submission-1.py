class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def addWord(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Trie()
            curr = curr.children[ch] 
        curr.end = True
    

    def findPrefix(self, prefix, word):
        curr = self
        if len(prefix) > len(word):
            return False
        index = 0
        for ch in prefix:
            if index < len(word) and ch != word[index]:
                return False
            elif ch not in curr.children:
                return False
            curr = curr.children[ch] 
            index += 1

        return True

    def findSuffix(self, suffix, word):
        curr = self
        if len(suffix) > len(word):
            return False
        index = 0
        for ch in suffix:
            if index < len(word) and ch != word[index]:
                return False
            elif ch not in curr.children:
                return False
            curr = curr.children[ch] 
            index += 1

        return True

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pairs = 0
        def isPrefix(prefix, word):
            if len(prefix) > len(word):
                return False
            return prefix == word[0:len(prefix)]

        def isSuffix(suffix, word):
            if len(suffix) > len(word):
                return False
            return suffix == word[len(word) - len(suffix):]
        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefix(words[i], words[j]) and isSuffix(words[i], words[j]):
                    pairs += 1

        return pairs

        
        