# https://www.acmicpc.net/problem/5622

numbers = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
s = input()
time = 0
for c in s:
    for num in numbers:
        if c in num:
            time += numbers.index(num) + 3
print(time)

# 숏코딩 참조
# print(sum(5*min(ord(x),88)//16-17for x in input()))
