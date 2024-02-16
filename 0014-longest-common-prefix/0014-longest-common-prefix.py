class Solution(object):
    def longestCommonPrefix(self, strs):
        len_lst = [len(i) for i in strs]
        min_len = min(len_lst)

        lst = [[] for i in range(min_len)]

        for l in range(len(lst)):
            for st in strs:
                lst[l].append(st[l])

        set_lst = [set(l) for l in lst]

        fi = []
        for i in range(len(set_lst)):
            if len(set_lst[i]) == 1:
                fi.append(set_lst[i])

            else:
                break

        st = ''
        for i in fi:
            st += (list(i)[0])

        return st



