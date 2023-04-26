from collections import defaultdict


def solution(genres, plays):
    answer = []

    total = defaultdict(int)
    album = defaultdict(list)
    for i in range(len(genres)):
        total[genres[i]] += plays[i]
        album[genres[i]].append([plays[i], i])

    total = sorted(list(total.items()), key=lambda x: x[1], reverse=True)
    for g, p in total:
        a = sorted(album[g], reverse=True, key=lambda x: x[0])[:2]
        answer += [x[1] for x in a]

    return answer


if __name__ == '__main__':
    # 해시, 베스트앨범 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/42579
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
    print(solution(["classic", "pop", "classic", "classic", "pop"], [800, 600, 150, 800, 2500]))
