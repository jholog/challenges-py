import heapq


def solution(program):
    program.sort(key=lambda x: x[1])

    h = []
    answer = [0] * 11
    start, now = -1, 0
    while program or h:
        while program:
            p = program.pop(0)
            if start < p[1] <= now:
                heapq.heappush(h, p)
            else:
                program.insert(0, p)
                break

        if h:
            score, call, runtime = heapq.heappop(h)
            answer[score] += (now - call)
            start = now
            now += runtime
        else:
            now += 1

    answer[0] = now

    return answer


if __name__ == '__main__':
    # 힙/우선순위큐, PCCP 모의고사 1회, 운영체제 문제
    # https://school.programmers.co.kr/learn/courses/15008/lessons/121686
    print(solution([[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]))
    print(solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]))
