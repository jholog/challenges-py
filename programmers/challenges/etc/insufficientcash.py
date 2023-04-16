def solution(price, money, count):
    total = sum(price * (i + 1) for i in range(count))
    return abs(money - total) if money < total else 0

if __name__ == '__main__':
    # 구현, 위클리 챌린지, 부족한 금액 계산하기 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/82612
    print(solution(3, 20, 4))
