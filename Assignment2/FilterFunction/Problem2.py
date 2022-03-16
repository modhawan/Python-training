from functools import reduce

lst1 = list(map(int, input().split(",")))
ans = reduce(lambda x,y: x*y, lst1)
print(ans)