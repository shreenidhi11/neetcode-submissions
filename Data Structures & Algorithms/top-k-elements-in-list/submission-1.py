class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq_map = Counter(nums)
        counter_list = [[] for _ in range(len(nums) + 1)]
        for num, count in freq_map.items():
            counter_list[count].append(num)
        for index in range(len(counter_list) - 1, -1, -1):
            for numbers in counter_list[index]:
                result.append(numbers)
                if len(result) == k:
                    return result

        return result
            
