def get_board_dimensions():
    while True:
        M, N = map(int, input().split())
        return M, N

def max_dominoes(M, N):
    if M % 2 == 0 and N % 2 == 0:
        return (M * N) // 2
    else:
        odd_dim, even_dim = (M, N) if M % 2 != 0 else (N, M)
        
        max_dominoes_complete = (even_dim * odd_dim) // 2
        
        if odd_dim > 1:
            return max_dominoes_complete + 1
        else:
            return max_dominoes_complete

M, N = get_board_dimensions()
print(max_dominoes(M, N))
