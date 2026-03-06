"""
362. Design Hit Counter
https://leetcode.com/problems/design-hit-counter/

Commonly asked at Atlassian (Premium)

Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that 
calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). 
Several hits may arrive roughly at the same time.

Implement the HitCounter class:
- HitCounter() Initializes the object of the hit counter system.
- void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may 
  happen at the same timestamp.
- int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp 
  (i.e., the past 300 seconds).

Example:
Input
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output
[null, null, null, null, 3, null, 4, 3]
"""

from collections import deque

class HitCounter:
    """
    Approach 1: Queue (Deque)
    Time: 
        hit: O(1)
        getHits: O(n) in worst case, but amortized O(1) since each hit is removed once
    Space: O(n) where n = number of hits in last 300 seconds
    """
    
    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        """Record a hit at timestamp"""
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """Get number of hits in last 300 seconds"""
        # Remove all hits older than 300 seconds
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        
        return len(self.hits)


class HitCounter_BucketArray:
    """
    Approach 2: Circular Array with Buckets
    Time: 
        hit: O(1)
        getHits: O(1) amortized
    Space: O(300) = O(1)
    
    More efficient for high-frequency hits at same timestamp
    """
    
    def __init__(self):
        self.times = [0] * 300  # Store timestamp for each bucket
        self.hits = [0] * 300   # Store hit count for each bucket

    def hit(self, timestamp: int) -> None:
        """Record a hit at timestamp"""
        idx = timestamp % 300
        
        if self.times[idx] != timestamp:
            # New 300-second window, reset this bucket
            self.times[idx] = timestamp
            self.hits[idx] = 1
        else:
            # Same second, increment count
            self.hits[idx] += 1

    def getHits(self, timestamp: int) -> int:
        """Get number of hits in last 300 seconds"""
        total = 0
        
        for i in range(300):
            # Only count if within 300 seconds
            if timestamp - self.times[i] < 300:
                total += self.hits[i]
        
        return total


# Test cases
if __name__ == "__main__":
    print("=== Test with Queue ===")
    counter = HitCounter()
    
    counter.hit(1)
    counter.hit(2)
    counter.hit(3)
    print(f"getHits(4): {counter.getHits(4)}")  # 3
    
    counter.hit(300)
    print(f"getHits(300): {counter.getHits(300)}")  # 4
    print(f"getHits(301): {counter.getHits(301)}")  # 3
    
    print("\n=== Test with Bucket Array ===")
    counter2 = HitCounter_BucketArray()
    
    counter2.hit(1)
    counter2.hit(2)
    counter2.hit(3)
    print(f"getHits(4): {counter2.getHits(4)}")  # 3
    
    counter2.hit(300)
    print(f"getHits(300): {counter2.getHits(300)}")  # 4
    print(f"getHits(301): {counter2.getHits(301)}")  # 3
    
    print("\n=== Test edge cases ===")
    counter3 = HitCounter()
    counter3.hit(1)
    counter3.hit(1)
    counter3.hit(1)
    counter3.hit(300)
    print(f"getHits(300): {counter3.getHits(300)}")  # 4
    print(f"getHits(301): {counter3.getHits(301)}")  # 1
