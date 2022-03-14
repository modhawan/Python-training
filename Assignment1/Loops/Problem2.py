n = int(input())
for upperRow in range(n):
    print(" " * (n - upperRow), "*" * (2 * upperRow + 1))
for lowerRow in range(n-2, -1, -1):
    print(" " * (n - lowerRow), "*" * (2 * lowerRow + 1))
    
