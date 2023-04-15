def solution(s):
    answer = True

    if len(s) != 4 and len(s) != 6:
        answer = False

    try:
        int(s)
    except:
        answer = False

    return answer

if __name__ == '__main__':
    # 문자열, 문자열 다루기 기본
    # https://school.programmers.co.kr/learn/courses/30/lessons/12918
    print(solution("a234"))
    print(solution("1234"))
    print(solution("54321"))
