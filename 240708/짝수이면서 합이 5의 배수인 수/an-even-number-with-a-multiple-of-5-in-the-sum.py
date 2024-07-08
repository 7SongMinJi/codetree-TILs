# # 문제를 top down으로 생각하기

# # 1부터 100 사이의 숫자들 중 3의 배수는 아니면서 5의 배수인 숫자의 개수를 세는 프로그램을 작성하기
# # 문제를 어떻게 풀지 큰 단위로 생각해보기
# 1. 1부터 100 사이의 숫자 i를 일일이 잡아본다
# 2. 숫자 i가 문제 조건에 맞는 숫자인지 보고, 그렇다면 개수를 1 증가시킨다
# 3. 답을 출력한다.
# cnt = 0
# for i in range(1, 101):
#     if is_magic_number(i):
#         cnt += 1
# print(cnt)

# # 즉, i가 문제 조건에 맞는 magic number인지만 판단해주는 함수만 잘 만들면 됨
# # 큰 단위의 코드를 먼저 작성해놓고, 그 다음 필요한 함수를 만들어 구현해주면 가독성 측면에서도 좋고 코드 작성시 발생하는 실수 역시 줄일 수 있음
# # 이 예에서는 is_magic_number 함수가 인자를 하나 받아, 해당 숫자가 특별한 숫자인지 / 아닌지를 판별하는 함수이므로 bool type인 True/False 중 하나를 반환하는 함수를 정의해주면 됨
# def is_magic_number(n):
#     return n % 3 != 0 and n % 5 == 0
# cnt = 0
# for i in range(1, 101):
#     if is_magic_number(i):
#         cnt += 1
# print(cnt)


# 문제

# 2자리 숫자 n이 주어졌을 때, n이 짝수이면서 각 자리 숫자의 합이 5의 배수이면 "Yes"를, 아니라면 "No"를 출력하는 프로그램 작성
# 단, 함수를 이용하여 문제를 해결할 것

def funcA(n):
    return n % 2 == 0 and (n // 10 + n % 10) % 5 == 0

n = int(input())
if funcA(n):
    print("Yes")
else:
    print("No")