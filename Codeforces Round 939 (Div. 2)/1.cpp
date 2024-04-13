def max_points(n, a, b):
    a.sort(reverse=True)
    b.sort(reverse=True)
    i = j = points = 0
    
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            points += 1
            i += 1
            j += 1
        else:
            j += 1
    
    return points

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    print(max_points(n, a, b))
