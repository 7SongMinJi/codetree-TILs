# # 함수가 또 다른 함수를 호출하는 경우

# # 두 자리 숫자 중 3의 배수는 아니면서 십의 자리 숫자와 일의 자리 숫자가 다른 수의 개수를 세는 프로그램 작성
# # 문제를 어떻게 풀지 큰 단위로 생각
# 1. 10부터 99 사이의 숫자 i를 일일이 잡아본다.
# 2. 숫자 i가 문제 조건에 맞는 숫자인지 보고, 그렇다면 개수를 1 증가시킨다.
# 3. 답을 출력한다.
# cnt = 0
# for i in range(10, 100):
#     if is_magic_number(i):
#         cnt += 1
# print(cnt)

# # is_magic_number 어떻게 구성할지 큰 단위로 생각하자
# 1. 3의 배수가 아니면서
# 2. 각 자리에 있는 숫자가 다른 경우에만 magic_number
# def is_magic_number(n):
#     return n % 3 != 0 and all_different(n)

# # all_different라는 함수 역시 정의가 필요함
# # 2자리에 해당하는 n만 주어지는 경우이므로, 십의 자리 수는 n을 10으로 나눈 몫, 일의 자리 수는 n을 10으로 나눴을 때의 나머지라는 점을 이용
# def all_different(n):
#     return (n // 10) != (n % 10)

# # 이렇듯 현재 풀려고 하는 문제가 복잡하다면, 크게 생각하여 이미 해당 함수가 주어져있다고 가정하고 코드를 작성한 뒤,
# # 이후에 실제 필요했던 함수를 작성해내는 식으로 진행하는 것이 좋음
# def all_different(n):
#     return (n // 10) != (n % 10)

# def is_magic_number(n):
#     return n % 3 != 0 and all_different(n)

# cnt = 0
# for i in range(10, 100):
#     if is_magic_number(i):
#         cnt += 1

# print(cnt)


# 문제

# 정수 a와 b가 주어지면, a 이상 b 이하 수들 중 3, 6, 9 중에 하나가 들어가 있거나 그 숫자 자체가 3의 배수인 숫자의 개수를 세는 프로그램 작성
# 단, 함수를 이용하여 문제를 해결할 것

a, b = tuple(map(int, input().split()))

def func(a, b):
    cnt = 0
    for i in range(a, b + 1, 1):
        if '3' in str(i) or '6' in str(i) or '9' in str(i) or i % 3 == 0:
            cnt += 1
    print(cnt)

func(a, b)