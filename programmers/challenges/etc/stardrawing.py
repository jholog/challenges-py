def solution(line):
    point = set()
    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(len(line)):
            if i == j:
                continue
            c, d, f = line[j]
            if (a * d - b * c) != 0:
                x = (b * f - e * d) / (a * d - b * c)
                y = (e * c - a * f) / (a * d - b * c)
                if x == int(x) and y == int(y):
                    point.add((int(x), int(y)))

    y_min, y_max = min(point, key=lambda x: x[1])[1], max(point, key=lambda x: x[1])[1]
    x_min, x_max = min(point, key=lambda x: x[0])[0], max(point, key=lambda x: x[0])[0]

    answer = [['.' for _ in range((x_max - x_min + 1))] for _ in range((y_max - y_min + 1))]
    for x, y in point:
        answer[y_max - y][x - x_min] = '*'

    return ["".join(a) for a in answer]


if __name__ == '__main__':
    # 구현, 위클리 챌린지, 교점에 별 만들기 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/87377
    print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
    print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
    print(solution([[1, -1, 0], [2, -1, 0]]))
    print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
