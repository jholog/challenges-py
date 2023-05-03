def dfs(root, maps):
    way = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    queue = [root]
    visited = [[[0 for _ in range(2)] for _ in range(len(maps[0]))] for _ in range(len(maps))]

    while queue:
        i, j, cnt, jump = queue.pop(0)

        if i == len(maps[0]) - 1 and j == len(maps) - 1:
            return cnt
        if not valid(i, j, maps):
            continue
        if maps[j][i] == 0:
            continue
        if visited[j][i][jump]:
            continue
        visited[j][i][jump] = 1

        for w in way:
            if valid(i + w[0], j + w[1], maps):
                if maps[j + w[1]][i + w[0]] == 0:
                    if jump:
                        queue.append([i + w[0] * 2, j + w[1] * 2, cnt + 1, 0])
                else:
                    queue.append([i + w[0], j + w[1], cnt + 1, jump])

    return -1


def valid(i, j, maps):
    if i < 0 or j < 0 or i > len(maps[0]) - 1 or j > len(maps) - 1:
        return False
    return True


def solution(n, m, hole):
    maps = [[1 for _ in range(n)] for _ in range(m)]
    for i, j in hole:
        maps[j - 1][i - 1] = 0

    return dfs([0, 0, 0, 1], maps)


if __name__ == '__main__':
    # bfs or dp, PCCP 모의고사 2회, 보물 지도
    # https://school.programmers.co.kr/learn/courses/15009/lessons/121690
    print(solution(4, 4, [[2, 3], [3, 3]]))
    print(solution(5, 4, [[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))
    print(solution(2, 2, [[1, 0], [0, 1]]))

# 조금 더 효율적인 다른 사람 풀이 참조
# from collections import deque
#
# def solution(n, m, hole):
#     # 가로 n 세로 m
#     dp = [[[-1, -1] for _ in range(m + 1)] for __ in range(n + 1)]
#     dp[1][1][0] = 0
#     # 지도 갈 수 없는 곳 1로 표시
#     mp = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
#     for x, y in hole: mp[x][y] = 1
#
#     # 시작점 큐에 삽입
#     q = deque()
#     q.append((1, 1, 0))
#
#     while q:
#         x, y, b = q.popleft()
#
#         for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             for s in range(2):
#                 if b == 1 and s == 1: continue
#                 # b가 1이면 점프 이미 씀, s가 1이면 점프 사용
#                 nx, ny, nb = x + dx * (s + 1), y + dy * (s + 1), b | s
#                 # 못가거나 방문함
#                 if nx < 1 or ny < 1 or nx > n or ny > m or mp[nx][ny] > 0 or dp[nx][ny][nb] != -1: continue
#
#                 q.append((nx, ny, nb))
#                 dp[nx][ny][nb] = dp[x][y][b] + 1
#
#     res = dp[n][m][1]
#     if res == -1 or (dp[n][m][0] >= 0 and res > dp[n][m][0]): res = dp[n][m][0]
#
#     return res
