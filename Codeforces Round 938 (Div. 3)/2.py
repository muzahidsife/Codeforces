def get_input():

    t = int(input())
    test_cases = []

    for _ in range(t):

        n, c, d = map(int, input().split())
        

        elements = list(map(int, input().split()))
        
        test_cases.append((n, c, d, elements))
    
    return test_cases
def is_progressive_square(n, c, d, elements):

    a1_1 = min(elements)
    

    square = [[a1_1 + i * c + j * d for j in range(n)] for i in range(n)]
    

    flat_square = [item for sublist in square for item in sublist]
    

    return sorted(elements) == sorted(flat_square)

test_cases = get_input()
for n, c, d, elements in test_cases:
    print("YES" if is_progressive_square(n, c, d, elements) else "NO")
