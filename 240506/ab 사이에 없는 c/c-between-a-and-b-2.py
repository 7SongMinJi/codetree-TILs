# # 모두 만족하는 경우

# # 하나라도 만족하는지 여부 = bool 변수 False로 두고 시작 & 조건 만족할 경우 True로 바꾸기
# # 모두 만족하는지 여부 = bool 변수 True로 두고 시작 & 조건 만족하지 않을 경우 False로 바꾸기

# arr = input().split()
# a, b = int(arr[0]), int(arr[1])

# satisfied = True
# for i in range(a, b + 1):
#     if i % 2 != 0:
#         satisfied = False

# if satisfied == True:
#     print("Satisfied")
# else:
#     print("Not satisfied")


# 문제
arr = input().split()

a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
bool_val = True

for i in range(a, b + 1):
    if i % c == 0:
        bool_val = False

if bool_val == True:
    print("YES")
else:
    print("NO")