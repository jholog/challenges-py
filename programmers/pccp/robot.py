def solution(command):
    answer = [0, 0]
    way = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    i = 0
    for c in command:
        if c == "R":
            i += 1
        elif c == "L":
            i -= 1
        else:
            j = 2 if c == "B" else 0
            answer[0] += way[(i + j) % 4][0]
            answer[1] += way[(i + j) % 4][1]

    return answer


if __name__ == '__main__':
    # PCCP 모의고사 2회, 실습용 로봇
    # https://school.programmers.co.kr/learn/courses/15009/lessons/121687
    print(solution("GRGLGRG"))
    print(solution("GRGRGRB"))
    print(solution("BBBBB"))
