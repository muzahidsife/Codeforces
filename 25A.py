n = int(input())

odd = []
even = []

numbers = list(map(int, input().split()))

for i in numbers:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)


even_index = None
odd_index = None

if len(even) == 1:
    even_index = numbers.index(even[0]) + 1  
if len(odd) == 1:
    odd_index = numbers.index(odd[0]) + 1  

if even_index is not None:
    print(even_index)
elif odd_index is not None:
    print(odd_index)