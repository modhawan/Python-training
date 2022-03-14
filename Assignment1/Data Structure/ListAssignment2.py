list1 = input().split(",")
list2 = input().split(",")
ans = []

for i in list1:
    for j in list2:
        ans.append(i+j)

print(ans)
