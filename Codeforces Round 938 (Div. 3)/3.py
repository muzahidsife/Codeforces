def kraken_attack(n, k, durability):
    sunk_ships = 0
    first_ship = 0
    last_ship = n - 1
    for attack in range(k):
        if first_ship > last_ship:  
            break
        if attack % 2 == 0:  
            if durability[first_ship] > 0:
                durability[first_ship] -= 1
                if durability[first_ship] == 0:
                    sunk_ships += 1
                    first_ship += 1
        else: 
            if durability[last_ship] > 0:
                durability[last_ship] -= 1
                if durability[last_ship] == 0:
                    sunk_ships += 1
                    last_ship -= 1

    return sunk_ships

def process_input_output():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n, k = map(int, input().strip().split())
        durability = list(map(int, input().strip().split()))
        results.append(kraken_attack(n, k, durability))
    print('\n'.join(map(str, results)))
process_input_output()
