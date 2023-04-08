def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    dupli = list(set(lost) & set(reserve))
    for d in dupli:
        lost.remove(d)
        reserve.remove(d)
    for r in reserve:
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)

    return n - len(lost)


if __name__ == '__main__':
    # 그리디 서치, 체육복 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/42862
    print(solution(5, [2, 4], [1, 3, 5]))
    print(solution(5, [2, 4], [3]))
    print(solution(3, [3], [1]))
    print(solution(13, [1, 2, 5, 6, 10, 12, 13], [2, 3, 4, 5, 7, 8, 9, 10, 11, 12]))
