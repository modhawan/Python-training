from oopsConcept.StringClass import StringClass


class PairsPossible(StringClass):
    def __init__(self, s):
        self.list = self.strToList(s)
        self.pairList = self.makePairs(list)

    def makePairs(self, list):
        return [[a, b] for idx, a in enumerate(list) for b in list[idx + 1:]]

    def printPair(self):
        for pair in self.pairList:
            print(pair[0], end=" ")
            print(pair[1])

