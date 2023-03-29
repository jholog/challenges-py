# https://www.acmicpc.net/problem/10951

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:     # EOFError or ValueError
        break

# lines = sys.stdin.readlines() >> 대량인 경우 속도 면에서 input()보다 유리
