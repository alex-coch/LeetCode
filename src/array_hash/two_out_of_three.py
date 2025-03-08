class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        # time O(n1+n2+n3) , space O(1)
        hm1 = set(nums1)
        hm2 = set(nums2)
        hm3 = set(nums3)
        hm12 = hm1.intersection(hm2)
        hm23 = hm2.intersection(hm3)
        hm13 = hm1.intersection(hm3)
        return list(hm12 | hm23 | hm13)

