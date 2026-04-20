class Twitter:

    def __init__(self):
        self.follower = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res= []
        minheap = []

        # adding the user itself in the follower map
        self.follower[userId].add(userId)

        # iterate through all the followers of the userid, Here I will get the followers of the user
        for followers in self.follower[userId]:
            # check if the follwer is present in tweetmap
            if followers in self.tweetMap:
                # get the index of their recent post 
                index_of_recent_post = len(self.tweetMap[followers]) -1
                # getting the recent post from all the follwers of the user_id
                count, tweetid = self.tweetMap[followers][index_of_recent_post]
                minheap.append([ count, tweetid, followers, index_of_recent_post-1])
        heapq.heapify(minheap)

        #
        while minheap and len(res) <10:
            count, tweetid, followers, index_of_recent_post = heapq.heappop(minheap)
            res.append(tweetid)
            if index_of_recent_post >= 0:
                count, tweetid = self.tweetMap[followers][index_of_recent_post]
                heapq.heappush(minheap, [count, tweetid, followers, index_of_recent_post-1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)

        
