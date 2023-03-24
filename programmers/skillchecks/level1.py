def solution(alist, blist):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(alist, blist)]
    return answer


if __name__ == '__main__':
    alist = [[1, 2], [2, 3]]
    blist = [[3, 4], [5, 6]]

    answer = solution(alist, blist)
    print(answer)
