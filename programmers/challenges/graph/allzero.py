import sys

sys.setrecursionlimit(10 ** 6)


def solution(a, edges):
    global answer

    if sum(a) != 0:
        return -1

    graph = [[] for _ in range(len(a))]
    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    answer = 0
    visited = [0] * len(a)

    def dfs(n):
        global answer

        visited[n] = 1
        for i in graph[n]:
            if not visited[i]:
                a[n] += dfs(i)
        answer += abs(a[n])

        return a[n]

    dfs(0)
    return answer


if __name__ == '__main__':
    # 완전 탐색(for loop, dfs, bfs)/그래프, 모두 0으로 만들기 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/76503
    print(10 ** 6)
    print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
    print(solution([0, 1, 0], [[0, 1], [1, 2]]))
