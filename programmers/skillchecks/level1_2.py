def solution(a, b):
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]  # 2016년 1월 1일은 금요일
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = 2016

    # check leap year
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        month[1] = 29

    i = (sum(month[:a - 1]) + b) % 7
    answer = day[i - 1]
    return answer


if __name__ == '__main__':
    a, b = 5, 24

    answer = solution(a, b)
    print(answer)
