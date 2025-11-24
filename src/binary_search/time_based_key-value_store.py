from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res, l, r = "", 0, len(self.hm[key]) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.hm[key][mid][0] <= timestamp:
                res = self.hm[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res

# # Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set("foo","bar",1)
# print(obj.get("foo",1))
# obj.set("foo","bar2",4)
# print(obj.get("foo",4))
# print(obj.get("foo",5))
