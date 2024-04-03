def execute_program(program):
    x = 0
    for statement in program:
        if "++" in statement:
            x += 1
        elif "--" in statement:
            x -= 1
    return x

n = int(input())
program = [input() for _ in range(n)]

final_value = execute_program(program)


print(final_value)
