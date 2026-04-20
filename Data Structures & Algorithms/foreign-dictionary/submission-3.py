class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #indegree for the characters
        indegree_words = {c:0 for word in words for c in word}
        # set is used to ensure avoid duplicates like hef her => f -> r(store)  ghf ghr => f -> r (not store)
        adj_list = defaultdict(set)
        result_order = []

        #build the order graph
        for index in range(len(words) - 1):
            word1, word2 = words[index], words[index + 1]
            min_length = min(len(word1), len(word2))

            # That means "abc" comes before "ab" in the given list, which is impossible in any valid dictionary order (a longer word can’t come before its prefix
            if len(word1) > len(word2) and word1[:min_length] == word2[:min_length]:
                return ""

            for j in range(min_length):
                if word1[j] != word2[j]:
                    if word2[j] not in adj_list[word1[j]]:
                        adj_list[word1[j]].add(word2[j])
                        indegree_words[word2[j]] += 1
                    #Only the first differing character matters.
                    # Once we find it, later characters don’t give any new ordering information.   
                    break

        # run normal topological sort
        queue = deque([ char for char, count in indegree_words.items() if count == 0])

        while queue:
            char = queue.popleft()
            result_order.append(char)
            for nei in adj_list[char]:
                indegree_words[nei] -= 1
                if indegree_words[nei] == 0:
                    queue.append(nei)

        
        if len(result_order) < len(indegree_words):
            return ""

        return "".join(result_order)
                

    # tc is O(N + V + E)
    # sc is O(V + E)




                        



        