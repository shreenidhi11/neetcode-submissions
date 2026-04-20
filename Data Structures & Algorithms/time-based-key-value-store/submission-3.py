class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        reslist = self.dict[key]
        res = ""
        if not reslist:
            return ""
        # [1,"alice"], ["4", "bob"], ["6", "mary"]
        l, r = 0, len(reslist)-1


        while l <= r:
            mid = (l+r) // 2
            if reslist[mid][0]  == timestamp:
                return reslist[mid][1]
            if reslist[mid][0] < timestamp:
                l = mid + 1
                res = reslist[mid][1]
            else:
                r = mid - 1

        return res





            



        
