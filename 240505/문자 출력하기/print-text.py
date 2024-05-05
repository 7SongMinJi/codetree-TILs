# # n번 반복하기

# # 그냥 단순히 n번 반복하고 싶다면 그냥 range(n)이라 쓰기!
# for i in range(n):
#     반복할 코드 작성

# n = int(input())
# for i in range(n):
#     print("A")

# # 반복 출력시 공백이나 줄바꿈 없이 출력하려면 end=""로 end값만 조정해주면 됨!
# n = int(input())
# for i in range(n):
#     print("A", end="")

# # 반복변수 i 대신 _로 써도 되나봄!
# n = int(input())

# for _ in range(n):
#     print("A", end="")


# 문제
x = input()
for _ in range(8):
    print(x, end="")