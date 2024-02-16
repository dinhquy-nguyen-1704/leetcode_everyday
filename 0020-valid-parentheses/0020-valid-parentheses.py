class Solution(object):
    def isValid(self, symbol_string):
        s = []
        balanced = True
        index = 0
        while balanced and index < len(symbol_string):
            symbol = symbol_string[index]
            if symbol in "([{":
                s.append(symbol)
            else:
                if s == []:
                    balanced = False
                else:
                    top = s.pop()
                    if "([{".index(top) != ")]}".index(symbol):
                        balanced = False

            index += 1

        if balanced and s == []:
            return True
        else:
            return False