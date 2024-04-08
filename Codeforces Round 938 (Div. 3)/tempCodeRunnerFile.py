def is_progressive_square(n, c, d, matrix):
    a_1_1 = matrix[0][0]
    for i in range(n):
        for j in range(n):
            expected_value = a_1_1 + i * c + j * d
            if matrix[i][j] != expected_value:
                return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n, c, d = map(int, input().split())
    elements = list(map(int, input().split()))
    matrix = [elements[i:i+n] for i in range(0, len(elements), n)]
    print(is_progressive_square(n, c, d, matrix))
