n = list(map(int, input().split()))

count = 0

for num in n:
    if num == 4 or num == 7:
        count += 1

if count == 4 or count == 7:
    print("YES")
else:
    print("NO")
