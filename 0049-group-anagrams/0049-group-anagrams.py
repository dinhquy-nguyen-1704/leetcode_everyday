class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        l = len(strs)
        new = []
        ans = []

        new_list = [sorted(i) for i in strs]

        for i in range(l):
            m = new_list[i]
            n = strs[i]
            if m not in new:
                ans.append([n])
                new.append(m)
            else:
                k = new.index(m)
                ans[k].append(n)

        return ans



