# # 단 하나라도 만족하는 경우

# # if, or 연산을 통해 판단 가능 but 범위 내에서 확인해야 할 경우 for문 필요
# # 여러 선택지들 중 단 하나라도 조건을 만족하는 경우가 있는지는 True, False 값을 갖는 bool type 변수를 활용해 해결 가능함
# # bool type 변수의 초기값을 False로 둔 다음, 조건을 만족한다면 해당 변수의 값을 True로 바꿔주면 조건 만족하는 경우가 있는지 확인 가능!

# arr = input().split()
# a, b = int(arr[0]), int(arr[1])

# satisfied = False
# for i in range(a, b + 1):
#     if i % 2 == 0:
#         satisfied = True

# if satisfied == True:
#     print("Exists")
# else:
#     print("Not exists")


# 문제
arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

exists = False

for i in range(a, b + 1):
    if i % c == 0:
        exists = True

if exists == True:
    print("YES")
else:
    print("NO")