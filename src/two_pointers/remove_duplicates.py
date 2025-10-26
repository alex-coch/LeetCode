class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        l, r = 0, 1
        while r < len(nums):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
            else:
                r += 1
        # for i in range(l+1, len(nums)):
        #     nums[i] = "_"
        print(nums)
        return l+1

print(Solution().removeDuplicates([1,1,2,2,3]))