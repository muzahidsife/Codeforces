a = int(input())
b = input()

x = []
count = 0

for char in b:
    x.append(char)

for i in range(len(x) - 1):
    if x[i] == x[i + 1]:
        count += 1

print(count)
