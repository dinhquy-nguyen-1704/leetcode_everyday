class Solution(object):
    def merge(self, nums1, m, nums2, n):
        l1 = len(nums1)

        for i in range(m, l1):
            nums1.pop()

        l2 = len(nums2)

        for j in range(n, l2):
            nums2.pop()

        for k in nums2:
            nums1.append(k)

        nums1.sort()

        return nums1

        
