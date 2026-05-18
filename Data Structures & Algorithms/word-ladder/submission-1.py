class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # mapping pattern -> words that differ by 1 character
        queue = deque([beginWord])
        wordList.append(beginWord)
        pattern_dict = defaultdict(list)
        for word in wordList:
            for index in range(len(word)):
                pattern = word[:index] + "*" + word[index + 1:]
                pattern_dict[pattern].append(word)
        
        visit = set([beginWord])
        sequence_length = 1

        while queue:
            for _ in range(len(queue)):
                current_word = queue.popleft()
                if current_word == endWord:
                    return sequence_length
                
                for index in range(len(current_word)):
                    pattern = current_word[:index] + "*" + current_word[index + 1:]
                    for neighbours in pattern_dict[pattern]:
                        if neighbours not in visit:
                            queue.append(neighbours)
                            visit.add(neighbours)
            sequence_length += 1

        
        return 0

                                


        