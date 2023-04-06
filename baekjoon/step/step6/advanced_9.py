# https://www.acmicpc.net/problem/1316

n = int(input())
for _ in range(n):
    w = input()
    s = set()
    pre = ""
    for c in w:
        if c != pre:
            pre = c
            if c not in s:
                s.add(c)
            else:
                n -= 1
                break
print(n)

# 숏코딩 참조
# print(sum([*x]==sorted(x,key=x.find)for x in open(0))-1)
# 학습 필요