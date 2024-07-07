# # 인자가 1개인 함수

# # 연속하여 별 5개를 출력하는 것을 n번 반복하는 경우
# # n에 따라 n개의 줄에 걸쳐 직사각형 모양으로 별을 출력해주는 함수를 이용하면
# # 가변적인 값이 주어졌을 때에 적절한 처리 가능함
# def print_n_lines(n):
#     코드 작성

# # <함수 인자가 존재하는 함수 정의>
# # 함수 이름 옆에 있는 소괄호 사이에 원하는 변수 이름을 하나 적으면 됨!
# # 위의 경우는 n개의 줄에 걸쳐 출력하는 문제였으므로, 편의상 n이라는 이름으로 적어준 것
# # 이렇게 함수를 정의할 때, 같이 적어주는 값을 "함수의 인자"라고 함
# # n을 받아, n개의 줄에 걸쳐 각각 5개의 별을 출력하는 함수
# def print_n_lines(n):
#     for _ in range(n):
#         print("*" * 5)

# # <함수 인자가 존재하는 함수 실행>
# # 함수의 실행을 위해서는 '함수이름(인자값)' 형태로 적어주기
# def print_n_lines(n):
#     for _ in range(n):
#         print("*" * 5)
    

# row_num = int(input())
# print_n_lines(row_num)


# 문제
def print_n_lines(n):
    for _ in range(n):
        print("12345^&*()_")


row_num = int(input())
print_n_lines(row_num)