class FreqStack:

    def __init__(self):
        self.stack = []
        # hashmap to map count of incoming values
        self.cnt = {}
        # key: count, value : list of all elements with that count value
        self.stacks = {}
        self.maxcount = 0
        

    def push(self, val: int) -> None:
        # set the count of the current val
        val_cnt = 1 + self.cnt.get(val, 0)
        self.cnt[val] = val_cnt

        # we need to decide where to put this value i.e in which stack

        # if the val_cnt is greater than the current maxcount then we need to create a new stack([]) of that count(key) in the stacks dict
        # or else simply append the val to its corresponding count(key) value
        if val_cnt > self.maxcount:
            self.stacks[val_cnt] = []
            self.maxcount = val_cnt
        self.stacks[val_cnt].append(val)


    def pop(self) -> int:
        res = self.stacks[self.maxcount].pop()
        # need to decrement the count of this value now from the self.cnt = {} first
        self.cnt[res] -= 1
        # also check if you need to decrease your maxcount value
        if not self.stacks[self.maxcount]:
            self.maxcount -= 1
        return res





        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()