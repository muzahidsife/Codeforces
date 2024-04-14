a = input().upper().split("WUB")

if a[0] == "":
    a = a[1:]

for i in range(len(a)):
    print(a[i], end=" ")