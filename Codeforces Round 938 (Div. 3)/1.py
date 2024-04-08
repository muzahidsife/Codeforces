
def min_cost(t, test_cases):
    for i in range(t):
        n, a, b = test_cases[i]
        if n % 2 == 0:
       
            print(min(n // 2 * b, n * a))
        else:

            print(min((n // 2) * b + a, n * a))

t = int(input())
test_cases = []
for _ in range(t):
    n, a, b = map(int, input().split())
    test_cases.append((n, a, b))

min_cost(t, test_cases)
