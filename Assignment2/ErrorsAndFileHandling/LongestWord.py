def longestWord(filename):
    res = []
    with open(filename, 'r') as file:
              wordList = file.read().split()
    maxLen = len(max(wordList, key=len))
    for word in wordList:
        if(len(word) == maxLen):
            res.append(word)
    return res
    #return [word for word in wordList if len(word) == max_len]

ans = longestWord('a.txt')
print(*ans)
