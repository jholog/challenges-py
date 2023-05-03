import heapq


def solution(ability, number):
    h = []
    for a in ability:
        heapq.heappush(h, a)

    for _ in range(number):
        x = heapq.heappop(h)
        y = heapq.heappop(h)
        heapq.heappush(h, x + y)
        heapq.heappush(h, x + y)

    return sum(list(h))


if __name__ == '__main__':
    # 힙, PCCP 모의고사 2회, 신입사원 교육
    # https://school.programmers.co.kr/learn/courses/15009/lessons/121688
    print(solution([10, 3, 7, 2], 2))
    print(solution([1, 2, 3, 4], 3))
