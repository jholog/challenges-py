def solution(s):
    words = s.upper().split(" ")    # 힌트에선 .split(" ", -1)을 써야 뒷부분 공백도 처리된다함
    print(words)
    s = []

    for w in words:
        w = list(w)
        for i in range(len(w)):
            if i % 2 == 1:
                w[i] = w[i].lower()
        s.append(''.join(w))

    return ' '.join(s)


if __name__ == '__main__':
    # 문자열, 이상한 문자 만들기 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/12930
    print(solution("  try hello  world  "))
