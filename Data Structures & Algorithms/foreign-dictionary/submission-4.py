class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # indegree_map
        indegree = {ch :0 for word in words for ch in word}
        adj_list = defaultdict(set)
        # support i get the same order from two different words
        result = []

        # process in pairs and build the graph
        for index in range(len(words) - 1):
            word1, word2 = words[index] , words[index + 1]
            min_length = min(len(word1), len(word2))

            # check the condition where the current two words are worth the order
            if len(word1) > min_length and word1[:min_length] == word2[:min_length]:
                return ""

            # add the dependencies
            for j in range(min_length):
                if word1[j] != word2[j]:
                    if word2[j] not in adj_list[word1[j]]:
                        adj_list[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break
            
        # use the toposort
        queue = deque([char for char, cnt in indegree.items() if cnt == 0])

        while queue:
            char = queue.popleft()
            result.append(char)
            for dep in adj_list[char]:
                indegree[dep] -=1
                if indegree[dep] == 0:
                    queue.append(dep)

        if len(result) < len(indegree):
            return ""


        return "".join(result)
    # sc is O(V + E)




                        



        