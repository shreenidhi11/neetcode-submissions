class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [(p, s) for p, s in zip(position, speed)]

        for p, s in sorted(pairs)[::-1]:
            time_to_reach = ((target - p) / s)
            stack.append(time_to_reach)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


