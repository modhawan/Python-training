from oopsConcept.PairsPossible import PairsPossible


class EqualSumPairs(PairsPossible):
    def __init__(self, s):
        self.s = s

    def printEqualSumPairs(self):
        charList = self.strToList(self, self.s)
        pairList = self.makePairs(charList)
        s = set()
        for i in pairList:
            s.add(sum(i))
        return len(s)