# cnt = 0

# while True:
#     n = int(input())
#     if n % 2 == 0:
#         if cnt == 3:
#             break
#         print(n // 2)
#         cnt += 1

# # 위와 같이 코드를 작성하면 출력 결과는 잘 나오지만 EOFError 런타임 에러가 뜸
# # 그 이유는 EOFError - 더 이상 받을 입력이 없음에도 input을 시도할 때 발생


cnt = 0

while True:
    try:
        n = int(input())
        if n % 2 == 0:
            if cnt == 3:
                break
            print(n // 2)
            cnt += 1
    except EOFError:
        break