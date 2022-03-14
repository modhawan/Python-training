# keys = ["Ten", "Twenty", "Thirty"]
# values = [10, 20, 30]
keys = list(map(int, input().split(",")))
values = list(map(int, input().split(",")))
if(len(keys) != len(values)):
    print("Please enter the right values")
else:
    ans = dict()
    for i in range(len(keys)):
        ans[keys[i]] = values[i]
    print(ans)
