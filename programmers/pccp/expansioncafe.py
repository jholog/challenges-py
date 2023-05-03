def solution(menu, order, k):
    answer = 0

    q = []
    now, complete = 0, 0
    while order:
        if now % k == 0:
            customer = order.pop(0)
            complete = now if complete < now else complete
            q.append(complete + menu[customer])
            complete += menu[customer]
        if q:
            t = q.pop(0)
            if t > now:
                q.insert(0, t)
            if len(q) > answer:
                answer = len(q)
        now += 1

    return answer


if __name__ == '__main__':
    # 큐, PCCP 모의고사 2회, 카페 확장
    # https://school.programmers.co.kr/learn/courses/15009/lessons/121689
    print(solution([5, 12, 30], [1, 2, 0, 1], 10))
    print(solution([5, 12, 30], [2, 1, 0, 0, 0, 1, 0], 10))
    print(solution([5], [0, 0, 0, 0, 0], 5))
    print(solution([5, 6, 7, 11], [1, 2, 3, 3, 2, 1, 1], 10))
