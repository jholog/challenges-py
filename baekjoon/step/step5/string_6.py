# https://www.acmicpc.net/problem/10809

alphabet = [-1] * 26
s = input()
for c in s:
    alphabet[ord(c) - 97] = s.index(c)
print(" ".join(map(str, alphabet)))
