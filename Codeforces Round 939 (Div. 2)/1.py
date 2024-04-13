def find_winners(k, q, a, n_list):
    results = []
    for n in n_list:
        players = list(range(1, n+1))
        while True:
            to_remove = [players[i-1] for i in a if i <= len(players)]
            if not to_remove:
                break
            players = [player for player in players if player not in to_remove]
        results.append(len(players))
    return results

test_cases = []

t = int(input().strip())
for _ in range(t):
    k, q = map(int, input().split())
    a = list(map(int, input().split()))
    n_list = list(map(int, input().split()))
    test_cases.append((k, q, a, n_list))

outputs = []

for case in test_cases:
    winners = find_winners(*case)
    outputs.append(winners)

for winners in outputs:
    print(' '.join(map(str, winners)))
