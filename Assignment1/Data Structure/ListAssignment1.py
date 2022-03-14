outerList = []
n = int(input())
while(n > 0):
    innerList = list(map(int, input().split(",")))
    outerList.append(innerList)
    n -= 1

for i in outerList:
    s = set()
    ans = {}
    for j in i:
        if j not in s:
            s.add(j)
        else:
            if(j not in ans):
                ans[j] = 2
            else:
                ans[j] += 1

    if(len(ans)>0):
        for k,v in ans.items():
            print(str(k) + " -> " + str(v), end=", ")
        print()

