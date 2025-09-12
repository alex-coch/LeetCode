class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        ms = []
        ms.append((temperatures[0], 0))
        hv = temperatures[0]
        for idx, item in enumerate(temperatures[1:], 1):
            if hv >= item:
                ms.append((item, idx))
                if item < hv:
                    hv = item
            else:
                while ms and ms[-1][0] < item:
                    t_item, t_idx = ms.pop()
                    result[t_idx] = idx - t_idx
                ms.append((item, idx))
                hv = item

        return result
