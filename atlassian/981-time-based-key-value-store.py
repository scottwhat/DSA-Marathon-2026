"""
981. Time Based Key-Value Store
https://leetcode.com/problems/time-based-key-value-store/

Commonly asked at Atlassian

Design a time-based key-value data structure that can store multiple values for the same key at 
different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:
- TimeMap() Initializes the object of the data structure.
- void set(String key, String value, int timestamp) Stores the key key with the value value at the 
  given time timestamp.
- String get(String key, int timestamp) Returns a value such that set was called previously, with 
  timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated 
  with the largest timestamp_prev. If there are no values, it returns "".

Example:
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]
"""

from collections import defaultdict

class TimeMap:
    """
    Time:
        set: O(1)
        get: O(log n) where n = number of timestamps for the key
    Space: O(n) where n = total number of set operations
    """
    
    def __init__(self):
        # key -> list of (timestamp, value) pairs
        # Timestamps are strictly increasing for each key
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """Store key-value with timestamp"""
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """Get value for key at or before timestamp"""
        if key not in self.store:
            return ""
        
        values = self.store[key]
        
        # Binary search for largest timestamp <= given timestamp
        left, right = 0, len(values) - 1
        result = ""
        
        while left <= right:
            mid = (left + right) // 2
            
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid + 1  # Look for larger timestamp
            else:
                right = mid - 1
        
        return result


class TimeMap_BisectVersion:
    """Alternative implementation using bisect module"""
    
    def __init__(self):
        from collections import defaultdict
        self.store = defaultdict(list)
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        import bisect
        values = self.store[key]
        
        # Find rightmost timestamp <= given timestamp
        i = bisect.bisect_right(values, (timestamp, chr(127)))
        
        return values[i-1][1] if i > 0 else ""


# Test cases
if __name__ == "__main__":
    timeMap = TimeMap()
    
    timeMap.set("foo", "bar", 1)
    print(f"get('foo', 1): {timeMap.get('foo', 1)}")  # "bar"
    print(f"get('foo', 3): {timeMap.get('foo', 3)}")  # "bar"
    
    timeMap.set("foo", "bar2", 4)
    print(f"get('foo', 4): {timeMap.get('foo', 4)}")  # "bar2"
    print(f"get('foo', 5): {timeMap.get('foo', 5)}")  # "bar2"
    
    print("\n--- Test 2 ---")
    timeMap2 = TimeMap()
    timeMap2.set("love", "high", 10)
    timeMap2.set("love", "low", 20)
    print(f"get('love', 5): {timeMap2.get('love', 5)}")   # ""
    print(f"get('love', 10): {timeMap2.get('love', 10)}")  # "high"
    print(f"get('love', 15): {timeMap2.get('love', 15)}")  # "high"
    print(f"get('love', 20): {timeMap2.get('love', 20)}")  # "low"
    print(f"get('love', 25): {timeMap2.get('love', 25)}")  # "low"
