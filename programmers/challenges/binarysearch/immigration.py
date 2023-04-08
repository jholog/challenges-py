def solution(n, times):
    # 시간의 최솟값을 return
    times.sort()
    low, high = 0, times[-1] * n
    while low <= high:
        mid = (low + high) // 2
        cnt = 0
        for t in times:
            cnt += mid // t

        if cnt < n: # 처리된 사람이 적음
            low = mid + 1
        else: # 처리된 사람이 많거나 알맞음
            high = mid - 1
            anwser = mid

    return anwser


if __name__ == '__main__':
    # 이분탐색, 입국심사 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/43238?language=python3
    print(solution(6, [7, 10]))
