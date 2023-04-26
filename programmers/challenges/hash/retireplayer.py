from collections import Counter


def solution(participant, completion):
    c = Counter(participant) - Counter(completion)
    return list(c.keys())[0]


if __name__ == '__main__':
    # 해시, 완주하지 못한 선수 문제
    # https://school.programmers.co.kr/learn/courses/30/parts/12077
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
    print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
