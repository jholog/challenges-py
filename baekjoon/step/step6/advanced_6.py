# https://www.acmicpc.net/problem/1157

from collections import Counter

d = dict(Counter(list(input().upper())))
k = list(d.keys())
v = list(d.values())
print("?") if v.count(max(v)) > 1 else print(k[v.index(max(v))])

# 숏코딩 참조
# s = input().upper()
# c = s.count
# *_, a, b = v = sorted({*s, '?'}, key=c)
# print(v[-(c(a) < c(b))])
