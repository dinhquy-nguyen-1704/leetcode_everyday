class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        self.x = x
        x_lst = [ch for ch in str(self.x)]
        if len(x_lst) == 1:
            return True
        lst = []
        for num in range((len(x_lst)//2)):
            if x_lst[num] == x_lst[-num - 1]:
                lst.append(x_lst)

            if len(lst) == len(x_lst)//2:
                return True

        return False

