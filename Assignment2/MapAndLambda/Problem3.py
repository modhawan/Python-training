lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
count_A = sum(map(lambda x: x.count("A"), lst1))
count_a = sum(map(lambda x: x.count("a"), lst1))
ans = [count_A,count_a]
print(ans)