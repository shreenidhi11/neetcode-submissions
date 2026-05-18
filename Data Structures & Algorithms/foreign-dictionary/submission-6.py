class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        indegree = {ch: 0 for word in words for ch in word}
        adj_list = defaultdict(set)
        result = []
        # building the adj_list
        for index in range(len(words) - 1):
            word1 = words[index]
            word2 = words[index + 1]
            word1_length = len(word1)
            word2_length = len(word2)
            min_length = min(word1_length, word2_length)
            if word1_length > min_length and word1[: min_length] == word2[:min_length]:
                return ""

            for j in range(min_length):
                if word1[j] != word2[j]:
                    if word2[j] not in adj_list[word1[j]]:
                        adj_list[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break

        # topo sort
        queue = deque([char for char, cnt in indegree.items() if cnt == 0])

        while queue:
            char = queue.popleft()
            result.append(char)
            for nei in adj_list[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        if len(result) < len(indegree):
            return ""

        return "".join(result)


        # O(N + V + e)
        # (V + E)