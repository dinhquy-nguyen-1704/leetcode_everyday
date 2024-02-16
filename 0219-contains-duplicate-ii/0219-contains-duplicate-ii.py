class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        dic = {}

        for key, val in enumerate(nums):
            if val not in dic:
                dic[val] = key

            else:
                if abs(dic.get(val) - key) <= k:
                    return True

                else:
                    dic[val] = key

        return False
