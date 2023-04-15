def solution(tickets):
    answer = []
    visited = [0] * len(tickets)

    def dfs(now, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return

        for i, ticket in enumerate(tickets):
            if ticket[0] == now and visited[i] == 0:
                visited[i] = True
                dfs(ticket[1], path + [ticket[1]])
                visited[i] = False

    dfs("ICN", ["ICN"])
    answer.sort()
    return answer[0]


if __name__ == "__main__":
    # dfs, 여행경로 문제
    # https://school.programmers.co.kr/learn/courses/30/lessons/43164
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
    print(solution([["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"],
                    ["BBB", "AAA"]]))
