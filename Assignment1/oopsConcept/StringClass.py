class StringClass:
    def __init__(self, s):
        self.s = s

    def length(self):
        return len(self.s)

    def strToList(self, s):
        return [ch for ch in self.s]
