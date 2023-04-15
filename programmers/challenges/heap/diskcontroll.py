import heapq

def solution(jobs):
    jobs.sort()

    h = []
    delay = []
    for job in jobs:
        heapq.heappush(h, job)

    x, y = heapq.heappop(h)
    answer = y
    runtime = y
    now = 0
    while True:
        if not h and not delay:
            break
        if now < runtime:
            if h:
                job = heapq.heappop(h)
                if job[1] < now:
                    heapq.heappush(h, job)
                else:
                    heapq.heappush(delay, job[::-1])
        else:
            if delay:
                y, x = heapq.heappop(delay)
            else:
                x, y = heapq.heappop(h)
            diff = runtime - x
            if diff < 0:
                diff = 0
            answer += y + diff
            runtime += y
        now += 1

    return answer // len(jobs)


if __name__ == '__main__':
    print(solution([[0, 3], [1, 9], [2, 6]]))
    print(solution([[7, 8], [3, 5], [9, 6]]))
    print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))
    print(solution([[0, 5], [2, 10], [10000, 2]]))
    print(solution([[0, 5], [2, 100], [2, 10]]))
