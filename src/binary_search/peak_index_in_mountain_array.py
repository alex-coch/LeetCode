class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1

print(Solution().peakIndexInMountainArray([0,1,0]))