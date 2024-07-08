# # 인자가 2개 이상일 때의 함수

# # 3개의 값이 주어졌을 때, 모두 합하여 반환해주는 add 함수 만들기
# def add(a, b, c):
#     return a + b + c

# print(add(1, 3, 5))

# # 위의 함수에, 2개의 인자 값만 넣어서 넘기면 다음과 같은 에러가 발생하게 됨. c에 적절한 값을 넘기지 않아 함수를 제대로 실행할 수 없다는 에러
# def add(a, b, c):
#     return a + b + c

# print(add(1, 3))
# >> TypeError: add() missing 1 required positional argument: 'c'

# # 이런 경우를 방지하기 위해서 기본값을 정해줄 수 있음
# # a, b, c 전부 값이 채워져 오는 경우에는 a + b + c를 계산해주고, a, b만 넘어온 경우에는 c값에 0을 넣어 a + b만 계산이 되게끔 하고 싶은 경우
# # 함수를 정의할 때 c=0이라고 적어주면 원하는 결과를 얻을 수 있음
# def add(a, b, c=0):
#     return a + b + c

# print(add(1, 3)) # 4
# print(add(1, 3, 5)) # 9


# # Side Note *****
# # 인자가 2개가 넘어오든, 3개, 4개 몇 개가 넘어오든 넘어온 값들의 합을 반환해주는 함수를 정의하는 것은 가능할까? O
# # *(asterisk)을 사용하면 인자 개수에 상관없이 tuple이라는 형태로 값들을 받아올 수 있게 됨
# def add(*args):
#     print(f"args: {args}")

# add(1, 2) # args: (1, 2)
# add(1, 2, 3) # args: (1, 2, 3)

# # 따라서 tuple 안에 있는 모든 숫자의 합은 sum 함수를 이용하여 계산이 가능함
# def add(*args):
#     return sum(args)

# add(1, 3, 2, 6, 5, 4) # 21


# 문제

# 세 정수 a, b, c가 주어지면 그 수를 전달받아 최솟값을 구하여 출력하는 프로그램 작성하기
# 이때 주어진 세 정수 a, b, c를 전달받아 최솟값을 구하는 함수를 작성하고, 주어진 a, b, c를 함수로 전달하여 출력함

a, b, c = tuple(map(int, input().split()))

def find_min(a, b, c):
    min_val = a
    if min_val > b:
        min_val = b
    if min_val > c:
        min_val = c
    return min_val

print(find_min(a, b, c))