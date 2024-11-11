sum = []

total = 0

k, n , w = map(int,input().split())

for i in range(1,w+1):
    sum.append(i*k)

for i in sum:
    total = total + i
    
if n >= total:
    print(0)
else:
    print(total-n)