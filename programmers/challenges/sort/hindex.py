def solution(citations):
    citations.sort(reverse=True)
    h = 0
    for c in citations:
        if c > h:
            h += 1
    # 참조할 만한 모범 답안
    # return max(map(min, enumerate(citations, start=1)))


if __name__ == '__main__':
    # 정렬, H-Index 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/42747
    print(solution([3, 0, 6, 1, 5]))
    print(solution([46, 328, 8344, 164, 1]))
    print(solution([1]))
    print(solution([0, 0, 0, 0, 0]))
    print(solution([3, 3, 4, 5, 1, 4, 0, 12, 1]))
