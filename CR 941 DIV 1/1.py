def winner_of_game(n, piles):
    if any(pile == 1 for pile in piles):
        return "Bob" if n % 2 == 0 else "Alice"
    else:
        return "Alice"
t = int(input())

inputs = []
outputs = []

for _ in range(t):
    n = int(input())
    piles = list(map(int, input().split()))
    inputs.append((n, piles))
    outputs.append(winner_of_game(n, piles))

for result in outputs:
    print(result)
