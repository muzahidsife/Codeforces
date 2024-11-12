n, k = map(int, input().split())
odd_count = (n + 1) // 2  
if k <= odd_count:
    print(2 * k - 1)
else:
    even_index = k - odd_count
    print(2 * even_index)
