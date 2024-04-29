def min_total_cost(t, test_cases):
    for s in test_cases:
        increasing_sequences = []
        current_sequence = [s[0]]
        for i in range(1, len(s)):
            if s[i] >= current_sequence[-1]:
                current_sequence.append(s[i])
            else:
                increasing_sequences.append(current_sequence)
                current_sequence = [s[i]]
        increasing_sequences.append(current_sequence)

        total_cost = 0
        for seq in increasing_sequences:
            total_cost += len(seq) - 1
        print(total_cost)

# Test case
test_cases = [
    "10",
    "0000",
    "11000",
    "101011",
    "01101001"
]
t = 5
min_total_cost(t, test_cases)


#wrong answer
