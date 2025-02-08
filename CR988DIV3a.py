n = int(input())
for i in range(n):
    m = int(input())
    a = list(map(int, input().split()))
    s = {}
    for i in a:
        if i in s:
            s[i] += 1
        else:
            s[i] = 1
    z = 0
    for i in s:
        z += s[i]//2

print(z)

