from collections import Counter


def solution(clothes):
    answer = 1
    for k, v in Counter(map(lambda x: x[1], clothes)).items():
        answer *= (v + 1)
    return answer - 1  # 최소 한 개의 의상은 착용하므로 모두 안 입는 경우의 수는 제외한다.


if __name__ == '__main__':
    # 해시, 의상 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/42578
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
    print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
