from itertools import permutations


def solution(k, dungeons):
    answer = -1

    for dungeon in permutations(dungeons):
        _k = k
        cnt = 0
        for require, cost in dungeon:
            if _k < require:
                break
            _k -= cost
            cnt += 1
        if answer < cnt:
            answer = cnt

    return answer


if __name__ == '__main__':
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))
