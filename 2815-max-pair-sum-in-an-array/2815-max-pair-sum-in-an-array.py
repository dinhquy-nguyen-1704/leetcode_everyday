class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        dic = {}
        n = len(nums)
        nums.sort()

        for i in nums:
            a = i
            m = 0
            while a != 0:
                m = max(a%10, m)
                a = a//10
            if m not in dic:
                dic[m] = [i]
            else:
                dic[m].append(i)

            m_list = []
            for j in dic:
                if len(dic[j]) > 1:
                    mx = dic[j][-1] + dic[j][-2]
                    m_list.append(mx)

        return max(m_list) if len(m_list) > 0 else -1

        
