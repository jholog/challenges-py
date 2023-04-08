def solution(distance, rocks, n):
    # 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return
    answer = 0
    rocks.sort()
    l, r = 1, distance
    while l <= r:
        mid = (l + r) // 2
        remove = 0
        pre = 0
        for rock in rocks:
            # 정답 결정 기준인 mid(최소 거리)보다 작으면 제거 필요
            if rock - pre < mid:
                remove += 1
            else:
                pre = rock
        if distance - pre < mid:
            remove += 1
        if remove <= n: # 너무 적게 제거 했거나 알맞음
            l = mid + 1
            answer = mid
        else:  # 너무 많이 제거 했음.
            r = mid - 1

    return answer


if __name__ == '__main__':
    # 이분탐색, 징검다리 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/43236
    print(solution(25, [2, 14, 11, 21, 17], 2))
    print(solution(18, [2, 8, 9, 10, 11, 12, 13], 6))
    print(solution(42, [0, 20, 30, 40, 41], 1))
