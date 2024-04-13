def calculate_maximum_points(cards):
    card_count = [0] * (len(cards) + 1)
    for card in cards:
        card_count[card] += 1
    points = sum(count // 2 for count in card_count)
    return points

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        cards = list(map(int, input().split()))
        results.append(calculate_maximum_points(cards))
    
    print()
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
