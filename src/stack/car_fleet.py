class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        hm = {position: speed for position, speed in zip(position, speed)}
        desc_sorted = sorted(hm.items(), reverse=True)
        stack = []
        for position, speed in desc_sorted:
            time_car = round((target - position) / speed, 1)
            if not stack:
                stack.append(time_car)
                continue
            if time_car > stack[-1]:
                stack.append(time_car)
        return len(stack)
