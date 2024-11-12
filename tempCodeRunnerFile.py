# Check if `d` or `nd` exists as a subsequence in `n`
if any(n[i:i+len(d)] == d for i in range(len(n) - len(d) + 1)):
    print("d")
elif any(n[i:i+len(nd)] == nd for i in range(len(n) - len(nd) + 1)):
    print("d")
else:
    print("n")