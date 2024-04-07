def solve():
    n = int(input())
    s = input()
    v = []
    count = 0

    if n == 2 and s == "00":
        print("YES")
        return

    if n == 2:
        print("NO")
        return

    if n == 1 and s == "0":
        print("YES")
        return

    if n == 1:
        print("NO")
        return

    for i in range(n):
        if s[i] == '1':
            count += 1
            v.append(i)

            if count == 2 and (v[1] - v[0]) == 1:
                print("NO")
                return

    if count % 2 == 0:
        print("YES")
    else:
        print("NO")

t = int(input())

for _ in range(t):
    solve()
