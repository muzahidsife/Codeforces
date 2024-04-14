import math

n = int(input())
groups = list(map(int, input().split()))

sum = 0


for i in range(len(groups)):
    sum += groups[i]

rr = sum/4
rounded_number = math.ceil(rr)


print(rounded_number)
