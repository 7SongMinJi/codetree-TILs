# 언제 끝날지 모르는 경우

# 특정 코드를 몇 번 반복해야 하는지 모르겠을 때 무한 루프 이용 & 원하는 조건을 만족했을 때 break로 반복문 탈출하도록 함

# 내가 적은 코드
# n = int(input())
# while True:
#     n //= 2
#     if n % 2 == 1:
#         print(n)
#         break

# 자료 코드
# n = int(input())
# while True:
#     print(f"current val is {n}")
#     if n % 2 == 0:
#         print("n is even")
#         n = n // 2
#     else:
#         print("n is odd")
#         break
# print(n)


# 문제
n = int(input())

cnt = 0

while True:
    if n == 1:
        break
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
    cnt += 1

print(cnt)

# 처음에는 틀림! n == 1일 때 바로 break하고 cnt... 암튼 여러 테스트 케이스에 대해 잘 따져보기