from collections import deque


def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while people:
        answer += 1
        if len(people) < 2:
            people.pop()
        elif people[0] + people[-1] > limit:
            people.pop()
        else:  # < limit
            people.pop()
            people.popleft()

    return answer


if __name__ == '__main__':
    # 그리디 서치, 구명보트 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/42885
    print(solution([70, 50, 80, 50], 100))
    print(solution([70, 80, 50], 100))
