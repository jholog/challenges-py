from collections import deque


def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    loc = deque([0] * len(priorities))
    loc[location] = 1
    while priorities:
        p = priorities.popleft()
        l = loc.popleft()
        if len(priorities) < 1:
            answer += 1
            break
        if p < max(priorities):
            priorities.append(p)
            loc.append(l)
        else:
            answer += 1
            if l == 1:
                break

    return answer


if __name__ == '__main__':
    # 큐 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/42587
    print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))
    print(solution([1], 0))
