# https://www.acmicpc.net/problem/25206

g_sum, s_sum = 0, 0
tb = ["F", "D", "C", "B", "A"]
for _ in range(20):
    g, s = input().split()[1:]
    if "P" in s:
        continue
    g_sum += float(g)
    s_sum += float(g) * (tb.index(s[0]) + 0.5 if '+' in s else tb.index(s[0]))
print(s_sum/g_sum)
