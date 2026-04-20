class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #The endword should be present in the wordlist
        if endWord not in wordList:
            return 0 

        #define a hashmap 
        neigh = collections.defaultdict(list)
        # add the word in your wordlist to start creating patterns
        wordList.append(beginWord)

        # create patterns 
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neigh[pattern].append(word)

        # create a visit set
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            # going layer by later
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                # find the neighbors of this word and add them in the queue
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    # you will get list, loop through that
                    # and add each of them in the queue
                    for p in neigh[pattern]:
                        if p not in visit:
                            visit.add(p)
                            q.append(p)

            res+=1
        
        return 0
                    




        
        


        
        