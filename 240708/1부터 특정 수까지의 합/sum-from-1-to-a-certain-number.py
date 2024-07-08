# # 값을 반환하는 함수

# # 다음과 같이 함수를 이용하면, 특정 인자값을 받아 원하는 값을 출력하는 것이 가능함
# def print_rect(n, m):
#     for _ in range(n):
#         print("*" * m)
# row_num, col_num = tuple(map(int, input().split()))
# print_rect(row_num, col_num)

# # 하지만 함수의 역할은, 꼭 출력해주는 것에만 국한되어 있지는 않음
# # 다음과 같이 두 수 a, b가 주어졌을 때 두 수의 합을 반환해주는 것 역시 함수가 할 수 있음
# # 어떤 함수가 값을 반환하기 위해서는, "return"이라는 키워드를 사용하면 됨
# def add(a, b):
#     return a + b
# # 위 함수는 합을 반환하는 함수이므로 이름을 add로 붙였고, 두 수 a, b의 합을 반환해야 하므로 return a + b를 적어주었음

# # 위와 같은 코드를 이용하면 다음과 같이 원하는 두 수의 합을 함수를 이용해 구할 수 있게 됨
# # add 함수를 호출한 이후의 결과를 total_num 변수에 넣어 출력한 예시
# def add(a, b):
#     return a + b

# num1, num2 = tuple(map(int, input().split()))
# total_num = add(num1, num2)

# print(total_num)


# 문제

# 정수 N이 주어지면 1부터 전달받은 수까지의 합을 10으로 나눈 값을 반환하는 함수를 작성하고, 함수로 전달하여 출력하는 프로그램 작성하기
# 단, 나머지는 버리고 몫만 출력함

def func_A(N):
    total = 0
    for i in range(1, N + 1, 1):
        total += i
    return (total // 10)

n = int(input())

print(func_A(n))