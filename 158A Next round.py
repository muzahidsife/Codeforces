x, y = map(int, input().split())
scores = list(map(int, input().split()))
count = 0
for i in scores:
    if i > 0 and i >= scores[y - 1]:
        count += 1
print(count)