from itertools import combinations


def solution(nums):
    # return max(map(lambda x: len(set(x)), list(combinations(nums, int(len(nums) / 2)))))
    sets = set(nums)
    return int(len(nums) / 2) if len(sets) > len(nums) / 2 else len(sets)


if __name__ == '__main__':
    # 해시, 폰켓몬
    # https://school.programmers.co.kr/learn/courses/30/lessons/1845
    print(solution([3, 1, 2, 3]))
    print(solution([3, 3, 3, 2, 2, 4]))
    print(solution([3, 3, 3, 2, 2, 2]))
