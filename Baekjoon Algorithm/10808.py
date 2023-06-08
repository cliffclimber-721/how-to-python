alphas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
S = list(str(input()))

for i in range(len(alphas)):
    word = S.count(alphas[i])
    print(word, end=' ')