n = int(input())

listt = [4,7,47,74,444,447,474,477,744,747,774,777]

m = 0

for i in listt:
    if n%i == 0:
        m += 1
        continue

if m > 0:
    print("YES")
else:
    print("NO")

    