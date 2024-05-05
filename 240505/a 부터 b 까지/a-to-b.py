# arr = input().split()

# a = int(arr[0])
# b = int(arr[1])

# for i in range(a, b + 1):
#     if i <= b and i % 2 == 1:
#         print(i, end=" ")
#         i *= 2
#     elif i <= b and i % 2 == 0:
#         print(i, end=" ")
#         i += 3
#     else:
#         pass


# 틀림... 다시
arr = input().split()

a, b = int(arr[0]), int(arr[1])

while(a <= b):
    print(a, end=" ")
    if a % 2 == 1:
        a *= 2
    else:
        a += 3
# 이번엔 맞음
# 이유는... for문의 반복변수 i는 반복문 수행 코드 내에서 i의 값이 바뀌어도 다음 반복 때 다시 range 값으로 재설정됨

# *****
# for 문을 사용하신 방식으로는 문제의 조건을 만족시키는 프로그램을 작성하기 어려움.
# 그 이유는 for 반복문에서 i의 값을 반복문 내에서 변경해도 다음 반복 때 range에 의해 정해진 값으로 i가 재설정되기 때문.
# 즉, i 값을 변경한다 해도 그 변경된 값이 다음 반복으로 이어지지 않음.

# 이 문제를 해결하려면, while 문을 사용하는 것이 적합함.
# while 문을 사용하면 초기 조건에서 설정한 변수의 값을 계속해서 업데이트하면서 조건에 맞을 때까지 반복할 수 있음.
# *****