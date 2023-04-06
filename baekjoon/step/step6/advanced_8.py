# https://www.acmicpc.net/problem/2941

alist = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
for c in alist:
    word = word.replace(c, "0")
print(len(word))

# 예제 입력 'ddz=z='의 경우 replace 적용 순서에 따라 길이가 다를 수 있음
