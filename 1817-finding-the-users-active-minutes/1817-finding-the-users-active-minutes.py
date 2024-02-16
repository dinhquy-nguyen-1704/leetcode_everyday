class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:

        dic = {}
        new_lst = []
        ans = [0]*k

        for i in logs:
            if i not in new_lst:
                new_lst.append(i)

        for i in new_lst:
            if i[0] not in dic:
                dic[i[0]] = 1

            else:
                dic[i[0]] += 1

        for i in dic:
            ans[dic[i] - 1] += 1

        return ans
