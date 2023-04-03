# https://www.acmicpc.net/problem/2562

alist = [int(input()) for _ in range(9)]    # int() 미적용 제출 시 오답
print(max(alist))
print(alist.index(max(alist)) + 1)