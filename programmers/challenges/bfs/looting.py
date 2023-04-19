from collections import deque


def solution(rectangle, cx, cy, ix, iy):
    def bfs(graph, cx, cy):
        way = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        queue = deque()
        queue.append((cx * 2, cy * 2, 0))

        while queue:
            x, y, cnt = queue.popleft()
            graph[x][y] = 1
            cnt += 1

            if (x, y) == (ix * 2, iy * 2):
                return cnt // 2

            for i, j in way:
                if graph[x + i][y + j] == 2:
                    queue.append((x + i, y + j, cnt))

        return -1

    graph = [[0] * 110 for _ in range(110)]

    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x1 < x < x2 and y1 < y < y2:
                    graph[x][y] = 1
                elif graph[x][y] != 1:
                    graph[x][y] = 2

    return bfs(graph, cx, cy)


if __name__ == '__main__':
    # bfs, 아이템 줍기 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/87694
    print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
    print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))
    print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))
    print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))
    print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))
