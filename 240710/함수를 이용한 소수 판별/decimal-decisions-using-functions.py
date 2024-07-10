# # 단 하나라도 만족/만족하지 않는 경우

# # 숫자 n이 소수인지를 판단하기 위해서는, 숫자 n이 2에서 n - 1까지 숫자들 중 단 하나라도 나누어 떨어지는지를 확인해야 함
# # 이렇듯 ** 단 하나라도 **라는 조건이 들어가는 경우에는, 다음과 같이 True/False 값을 갖는 bool 타입의 변수를 하나 선언하여 해결!!! ***
# n = 17

# is_prime = True
# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False

# if is_prime:
#     print("Prime")
# else:
#     print("Not Prime")

# # 하지만 소수인지 아닌지를 판단하는 이 과정을 함수를 이용하면 깔끔하게 작성이 가능함
# # 함수는 아직 함수 내에 있는 모든 코드를 수행하지 못했더라도 return을 만나게 되면 그 즉시 종료되기 때문에,
# # 이 특성을 이용하면 다음과 같이 숫자 n이 소수인지에 대한 여부를 손쉽게 작성할 수 있음
# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True

# # for loop을 돌며 단 한번이라도 숫자 n이 2부터 n-1사이의 숫자들로 나누어 떨어진다면
# # 바로 return 구문에 걸려 소수가 아니라는 의미의 False 값이 반환이 될 것이고,
# # 모두 나누어 떨어지지 않는다면 최종적으로 for loop을 빠져나와 True 값을 반환하게 될 것임
# # 이러한 함수를 이용하면 bool 변수 없이도 다음과 같이 숫자 n이 소수인지에 대한 여부를 알 수 있게 됨
# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
    
#     return True

# n = 17
# if is_prime(n):
#     print("Prime")
# else:
#     print("Not Prime")


# 문제

# 정수 a와 b가 주어지면, a 이상 b 이하 소수들의 합을 구해주는 프로그램을 작성하기
# 단, 함수를 이용하여 문제 해결하기

a, b = tuple(map(int, input().split()))

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n, 1):
        if n % i == 0:
            return False
    return True

def func_prime(a, b):
    sum = 0
    for i in range(a, b + 1, 1):
        if is_prime(i):
            sum += i
    return sum

print(func_prime(a, b))