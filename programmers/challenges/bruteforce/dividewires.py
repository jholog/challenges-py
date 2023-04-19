from collections import deque


def bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue.extend(graph[n])

    return len(visited)


def solution(n, wires):
    answer = 10 ** 6
    wires.sort()  # 테이스 케이스 8번이 실패 > 정렬 추가 후 통과.. 무슨 영향을 주는지 모르겠음

    for i in range(n - 1):
        wire = wires[:i] + wires[i + 1:]
        graph = [[] for _ in range(n + 1)]
        for v1, v2 in wire:
            graph[v1].append(v2)
            graph[v2].append(v1)
        cnt = bfs(graph, i)
        diff = abs(n - cnt - cnt)
        answer = diff if diff < answer else answer

    return answer


if __name__ == '__main__':
    # 완전탐색/bfs, 전력망을 둘로 나누기 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/86971
    print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
    print(solution(4, [[1, 2], [2, 3], [3, 4]]))
    print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
    print(solution(4, [[1, 2], [3, 4], [2, 3]]))
