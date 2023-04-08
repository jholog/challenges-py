import copy


def solution(name):
    name = list(name)
    cursor = [-1, 1]

    def dfs(root):
        stack = [root]

        while stack:
            s = stack.pop()
            arr, idx, cnt = s[0], s[1], s[2]
            cnt += min(ord(arr[idx]) - 65, 91 - ord(arr[idx]))
            arr[idx] = 'A'
            if arr.count('A') == len(arr):
                return cnt
            for way in cursor:
                _arr = copy.deepcopy(arr)
                _idx = idx + way
                _cnt = cnt + 1
                stack.insert(0, (_arr, _idx, _cnt))

    return dfs((name, 0, 0))

if __name__ == '__main__':
    # dfs/스택, 조이스틱 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/42860
    print(solution("JEROEN"))
    print(solution("JAN"))
    print(solution("AAA"))
