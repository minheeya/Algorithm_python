def solution(phone_book):

    N = len(phone_book) #전화번호 개수
    phone_book.sort() #정렬하면 접두사인 관계끼리 붙어있게 된다.

    for i in range(N-1):
        n = len(phone_book[i])
        if len(phone_book[i+1]) > n and phone_book[i+1][:n] == phone_book[i]:
            return False

    return True

