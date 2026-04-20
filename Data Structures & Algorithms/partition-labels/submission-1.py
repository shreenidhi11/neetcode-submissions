class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        recentIndex = defaultdict(int)
        for index in range(len(s)):
            recentIndex[s[index]] = index

        length = 0
        end_index = 0
        result = []
        r = 0
        for ch_index in range(len(s)):
            end_index = max(end_index, recentIndex[s[ch_index]])
            length += 1

            if ch_index == end_index:
                result.append(length)
                length = 0
        
        return result

        


        