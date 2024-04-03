def solve_contest(n, problems):
    count = 0
    for problem in problems:
        if sum(problem) >= 2:
            count += 1
    return count


n = int(input())
problems = []
for _ in range(n):
    problems.append(list(map(int, input().split())))

print(solve_contest(n, problems))
