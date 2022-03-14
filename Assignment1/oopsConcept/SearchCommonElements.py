from oopsConcept.PairsPossible import PairsPossible


class SearchCommonElements(PairsPossible):
    def __init__(self, s):
        self.s = s

    def findCommonElements(self):
        charList = self.strToList(self, self.s)
        dic = {}
        ans = []
        for char in charList:
            if(char not in dic):
                dic[char] = 1
            else:
                dic[char] += 1
        for key, value in dic.items():
            if(value > 1):
               ans.append(key)
        return ans

