n = int(input())
for row in range(1, n + 1):
    val = 1
    for col in range(1, row + 1):
        print(val, end=" ")
        val = int(val * (row - col) / col)
    for j in range(row + 1, n + 1):
        print(0, end=" ")
    print("")