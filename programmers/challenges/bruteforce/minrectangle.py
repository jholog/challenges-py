def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        w.append(max(sizes[i]))
        h.append(min(sizes[i]))
    return max(w) * max(h)


if __name__ == '__main__':
    # 완전탐색, 최소직사각형 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/86491
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
    print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
