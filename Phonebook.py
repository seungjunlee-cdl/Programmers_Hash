def solution(phone_book):
    phoneBook = sorted(phone_book)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
