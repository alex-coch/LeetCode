from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # time O(n), space O(n)
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

        freq = [[] for _ in range(len(nums) + 1)]

        for n, f in counter.items():
            freq[f].append(n)

        res = []

        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # time O(nlogn), space O(n)
        # hmap = defaultdict(int)
        # for num in nums:
        #     hmap[num] += 1
        # res = sorted(hmap.items(), key=lambda x: x[1], reverse=True)[:k]
        # return [item[0] for item in res]

        # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #     return [x for x, y in Counter(nums).most_common(k)]

print(Solution().topKFrequent([3,0,1,0], 1))

items = [(3, 1), (0, 2), (1, 1)]

# Sort the list by the second element of each tuple
sorted_items = sorted(items, key=lambda item: item[1])

# Print the sorted list
print(sorted_items)