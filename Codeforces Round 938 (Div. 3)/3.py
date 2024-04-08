def kraken_attack(n, k, durability):
    sunk_ships = 0
    first_ship = 0
    last_ship = n - 1
    while first_ship <= last_ship and durability[first_ship] == 0:
        first_ship += 1
        sunk_ships += 1
    while last_ship >= first_ship and durability[last_ship] == 0:
        last_ship -= 1
        sunk_ships += 1

    for attack in range(k):
        if first_ship > last_ship:
            break
        if attack % 2 == 0:
            if durability[first_ship] > 0:
                durability[first_ship] -= 1
                if durability[first_ship] == 0:
                    sunk_ships += 1
                    first_ship += 1
                    while first_ship <= last_ship and durability[first_ship] == 0:
                        first_ship += 1
                        sunk_ships += 1
        else:
            if durability[last_ship] > 0:
                durability[last_ship] -= 1
                if durability[last_ship] == 0:
                    sunk_ships += 1
                    last_ship -= 1
                    while last_ship >= first_ship and durability[last_ship] == 0:
                        last_ship -= 1
                        sunk_ships += 1

    return sunk_ships

def simulate_input_output(test_cases):
    results = []
    for n, k, durability in test_cases:
        results.append(kraken_attack(n, k, durability))
    return results

def main():
    num_cases = int(input())
    test_cases = []
    for _ in range(num_cases):
        n, k = map(int, input().split())
        durability = list(map(int, input().split()))
        test_cases.append((n, k, durability))

    results = simulate_input_output(test_cases)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
