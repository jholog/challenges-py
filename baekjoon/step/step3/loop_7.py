# https://www.acmicpc.net/problem/11021

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        print("Case #" + str(i+1) + ": " + str(a + b))
