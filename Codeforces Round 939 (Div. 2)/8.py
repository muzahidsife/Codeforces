def maximize_array_sum(a):
    n = len(a)
    operations = []
    current_sum = sum(a)
    max_sum = current_sum

    # Function to find the MEX of a subarray
    def mex(subarray):
        for i in range(len(subarray) + 1):
            if i not in subarray:
                return i

    # Main logic to maximize the sum
    for _ in range(5 * 10**5):
        for l in range(n):
            for r in range(l, n):
                subarray = a[l:r+1]
                x = mex(subarray)
                if x > 0:
                    operations.append((l+1, r+1))
                    for i in range(l, r+1):
                        a[i] = x
                    current_sum = sum(a)
                    if current_sum > max_sum:
                        max_sum = current_sum
                    break
            else:
                continue
            break
        else:
            break

    return max_sum, operations

# Example usage:
a = [1, 100, 2, 1]
max_sum, ops = maximize_array_sum(a)
print(max_sum, len(ops))
for op in ops:
    print(op[0], op[1])
