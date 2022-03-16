a, b, c, x = map(int, input().split(","))
quadraticEq = lambda a, b, c, x: a*x**2+b*x+c
print(quadraticEq(a, b, c, x))