lst1 = list(map(int, input().split(",")))
lst2 = list(filter(lambda x: True if x > 0 else False, map(lambda x: x*-1, lst1)))
print(lst2)