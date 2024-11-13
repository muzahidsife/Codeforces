a,b,c,d = map(int, input().split())

x = a * 60 + b
y = c* 60+ d
z = y - x

if x - y == 0:
    print("f")
else:
    print()