from collections import deque


def solution(maps):
    def bfs(maps, i, j):
        queue = deque()
        queue.append((i, j, 1))
        while queue:
            i, j, cnt = queue.popleft()

            if i == len(maps) - 1 and j == len(maps[0]) - 1:
                return cnt
            if maps[i][j] == 0:
                continue
            maps[i][j] = 0
            if i - 1 >= 0:  # 상
                queue.append([i - 1, j, cnt + 1])
            if i + 1 < len(maps):  # 하
                queue.append([i + 1, j, cnt + 1])
            if j - 1 >= 0:  # 좌
                queue.append([i, j - 1, cnt + 1])
            if j + 1 < len(maps[0]):  # 우
                queue.append([i, j + 1, cnt + 1])

        return -1

    return bfs(maps, 0, 0)


if __name__ == '__main__':
    # bfs, 게임 맵 최단거리
    # https://school.programmers.co.kr/learn/courses/30/lessons/1844
    print(solution([[1, 0, 1, 1, 1],
                    [1, 0, 1, 0, 1],
                    [1, 0, 1, 1, 1],
                    [1, 1, 1, 0, 1],
                    [0, 0, 0, 0, 1]]))
    print(solution([[1, 0, 1, 1, 1],
                    [1, 0, 1, 0, 1],
                    [1, 0, 1, 1, 1],
                    [1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 1]]))
