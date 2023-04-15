import heapq

def solution(jobs):
    jobs.sort()

    h = []
    answer, now, clear = 0, 0, 0
    start = -1

    while clear < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(h, job[::-1])

        if h:
            y, x = heapq.heappop(h)
            start = now
            now += y
            answer += now - x
            clear += 1
        else:
            now += 1

    return answer // len(jobs)




if __name__ == '__main__':
    # heap, 디스크 컨트롤러 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/42627
    print(solution([[0, 3], [1, 9], [2, 6]]))
    print(solution([[7, 8], [3, 5], [9, 6]]))
    print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))
    print(solution([[0, 5], [2, 10], [100, 2], [101, 3]]))
    print(solution([[0, 5], [2, 100], [2, 10]]))
