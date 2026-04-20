class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #indegree for the characters
        indegree_words = {c:0 for word in words for c in word}
        adj_list = defaultdict(set)
        result_order = []

        #build the order graph
        for index in range(len(words) - 1):
            word1, word2 = words[index], words[index + 1]
            min_length = min(len(word1), len(word2))

            # condition check
            if len(word1) > len(word2) and word1[:min_length] == word2[:min_length]:
                return ""

            for j in range(min_length):
                if word1[j] != word2[j]:
                    if word2[j] not in adj_list[word1[j]]:
                        adj_list[word1[j]].add(word2[j])
                        indegree_words[word2[j]] += 1
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
                




                        



        