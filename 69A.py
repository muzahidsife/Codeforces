n = int(input())  # Number of force vectors

x_sum = y_sum = z_sum = 0

for _ in range(n):
    x, y, z = map(int, input().split())
    x_sum += x
    y_sum += y
    z_sum += z

# If all sums are zero, print "YES", otherwise print "NO"
if x_sum == 0 and y_sum == 0 and z_sum == 0:
    print("YES")
else:
    print("NO")
