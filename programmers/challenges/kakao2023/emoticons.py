from itertools import product


def solution(users, emoticons):
    max_join = 0
    max_price = 0

    discounts = product([0.1, 0.2, 0.3, 0.4], repeat=len(emoticons))
    for discount in discounts:
        join = 0
        price = 0
        for user in users:
            sum = 0
            rate = user[0] * 0.01
            limit = user[1]
            for i in range(len(emoticons)):
                if discount[i] >= rate:
                    sum += emoticons[i] - (emoticons[i] * discount[i])
            if sum >= limit:
                join += 1
            else:
                price += int(sum)
        if join > max_join:
            max_join = join
            max_price = price
        elif join == max_join and price > max_price:
            max_price = price

    return [max_join, max_price]


if __name__ == '__main__':
    # 완전탐색 순열 문제, 이모티콘 할인행사 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/150368
    users = [[40, 10000], [25, 10000]]
    emoticons = [7000, 9000]
    print(solution(users, emoticons))
    users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
    emoticons = [1300, 1500, 1600, 4900]
    print(solution(users, emoticons))
