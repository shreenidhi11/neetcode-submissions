class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # create a hashmap of every character
        charset = {c:set() for w in words for c in w}

        # create the adjacency list now. this adjacency list will
        # contain the order of the characters.
        # we will take 2 words at a time to find the order

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minlen = min(len(w1), len(w2))

            # for example prevs and prev
            if len (w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""

            for j in range(minlen):
                if w1[j] != w2[j]:
                    charset[w1[j]].add(w2[j])
                    break

        visit = {}
        res= []
        def dfs(ch):
            if ch in visit:
                return visit[ch]

            visit[ch] = True

            for nei in charset[ch]:
                # checks for loops.
                # we get loops if we visit the same character twice
                # in the current dfs path
                if dfs(nei):
                    return True

            visit[ch] = False
            res.append(ch)

        for ch in charset:
            if dfs(ch):
                return ""

        res.reverse()
        return "".join(res)

        


            



        