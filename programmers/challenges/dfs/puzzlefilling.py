def dfs(graph, root, target):
    way = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    visited = []
    stack = [root]

    while stack:
        y, x = stack.pop()
        if [y, x] in visited:
            continue
        visited.append([y, x])
        if graph[y][x] != target:
            return
        graph[y][x] = 0 if target else 1
        for i, j in way:
            if 0 <= y + i < len(graph) and 0 <= x + j < len(graph):
                if graph[y + i][x + j] == target:
                    stack.append([y + i, x + j])

    return build(visited)


def build(arr):
    y = set(map(lambda x: x[0], arr))
    x = set(map(lambda x: x[1], arr))
    n = max(len(y), len(x))
    result = [[0 for _ in range(len(x))] for _ in range(len(y))]

    for j, i in arr:
        result[j - min(y)][i - min(x)] = 1

    return result


def spin(arr):
    n_y = len(arr)
    n_x = len(arr[0])
    result = [[0] * n_y for _ in range(n_x)]
    for y in range(n_y):
        for x in range(n_x):
            result[x][n_y - 1 - y] = arr[y][x]

    return result


def solution(board, table):
    answer = 0

    empty = []
    for i in range(len(board)):
        for j in range(len(board)):
            e = dfs(board, [i, j], 0)
            if e:
                empty.append(e)

    block = []
    for i in range(len(table)):
        for j in range(len(table)):
            b = dfs(table, [i, j], 1)
            if b:
                block.append(b)

    for b in block:
        tmp = [b := spin(b) for _ in range(4)]
        for e in empty:
            if e in tmp:
                answer += sum(map(lambda x: sum(x), e))
                empty.remove(e)
                break

    return answer


if __name__ == '__main__':
    # dfs, 퍼즐 조각 채우기 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/84021
    print(solution([[1, 1, 0, 0, 1, 0],
                    [0, 0, 1, 0, 1, 0],
                    [0, 1, 1, 0, 0, 1],
                    [1, 1, 0, 1, 1, 1],
                    [1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 0]],
                   [[1, 0, 0, 1, 1, 0],
                    [1, 0, 1, 0, 1, 0],
                    [0, 1, 1, 0, 1, 1],
                    [0, 0, 1, 0, 0, 0],
                    [1, 1, 0, 1, 1, 0],
                    [0, 1, 0, 0, 0, 0]]))
    print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]))
    print(solution([[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
                    [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
                    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
                    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
                    [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0],
                    [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
                    [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
                    [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]],
                   [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
                    [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
                    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
                    [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
                    [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                    [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
                    [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
                    [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
                    [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
                    [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]))
