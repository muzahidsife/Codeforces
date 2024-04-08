def count_good_subsegments(n, m, k, a, b):
    good_count = 0
    b_count = {x: 0 for x in b}
    for x in b:
        b_count[x] += 1

    for i in range(m):
        if a[i] in b_count:
            b_count[a[i]] -= 1
            if b_count[a[i]] == 0:
                del b_count[a[i]]

    if len(b_count) == k:
        good_count += 1

    for i in range(1, n - m + 1):
        if a[i - 1] in b_count:
            b_count[a[i - 1]] += 1
            if b_count[a[i - 1]] == 0:
                del b_count[a[i - 1]]
        if a[i + m - 1] in b_count:
            b_count[a[i + m - 1]] -= 1
            if b_count[a[i + m - 1]] == 0:
                del b_count[a[i + m - 1]]

        if len(b_count) == k:
            good_count += 1

    return good_count
