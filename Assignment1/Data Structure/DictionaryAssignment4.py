orignal = {"HuEx": [1,3,4],"is":[7,6],"best":[4,5]}
ans = []
for i in orignal:
    res = []
    res.append(i)
    temp = orignal.get(i)
    res.extend(temp)
    ans.append(res)
print(ans)
