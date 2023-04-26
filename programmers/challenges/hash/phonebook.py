def solution(phone_book):
    phone_book.sort()

    for s1, s2 in zip(phone_book, phone_book[1:]):
        if s2.startswith(s1):
            return False

    return True


if __name__ == '__main__':
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123", "456", "789"]))
    print(solution(["12", "123", "1235", "567", "88"]))
