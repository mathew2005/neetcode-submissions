# post tweets
# follow/unfollow each other
# 10 most recent tweets within their own news feed
from collections import defaultdict
from heapq import heapify, heappush, heappop
class Twitter:

    def __init__(self):
        self.following = defaultdict(set) #{userId: [ppl they follow]}
        self.tweets = defaultdict(list) #{userId: [(order, tweetId)]}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.following[userId].add(userId)
        self.tweets[userId].append((self.count,tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        heapify(maxHeap)
        
        user = self.following[userId] #gives us a list of all ppl they follow
        for followingId in user:
            for count,tweetId in self.tweets[followingId]:
                if len(maxHeap) < 10:
                    heappush(maxHeap,(count,tweetId))
                elif maxHeap[0][0] < count:
                    heappop(maxHeap)
                    heappush(maxHeap, (count,tweetId))
                
        res = []
        while maxHeap: res.append(heappop(maxHeap)[1])
        res.reverse()
        return res




    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
