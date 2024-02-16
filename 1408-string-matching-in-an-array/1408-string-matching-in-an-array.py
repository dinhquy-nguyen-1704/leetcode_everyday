class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        dic = {i:len(i) for i in words}
        le = len(words)
        ans = []

        l = list(sorted(dic.items(), key = lambda x:x[1]))
        lst = [i[0] for i in l]

        for i in range(le-1):
            length1 = len(lst[i])
            for j in range(i+1, le):
                length2 = len(lst[j])
                for k in range(length2 - length1 + 1):
                    if lst[j][k:k+length1] == lst[i] and lst[i] not in ans:
                        ans.append(lst[i])

        return ans


