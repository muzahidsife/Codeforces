def main():
    t = int(input())
    for _ in range(t):
        k = int(input())  
        shuffled = list(map(int, input().split())) 
        freq = {}
        for num in shuffled:
            freq[num] = freq.get(num, 0) + 1
        n = 1
        m = k
        for i in range(1, k + 1):
            if i in freq and freq[i] < m:
                n = freq[i]
                m = freq[i]
        print(n, m)

if __name__ == "__main__":
    main()
