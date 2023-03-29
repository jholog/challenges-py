# https://www.acmicpc.net/problem/10952

# while True:
#     a, b = map(int, input().split())
#     if a == 0 or b == 0:
#         break
#     print(a + b)

# walrus operator(:=) in Python 3.8
while a := eval("+".join(input().split())):
    print(a)
