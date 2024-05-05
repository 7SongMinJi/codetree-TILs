# x_input = input().split()
# x_cold, x_temp = x_input[0], int(x_input[1])

# y_input = input().split()
# y_cold, y_temp = y_input[0], int(y_input[1])

# z_input = input().split()
# z_cold, z_temp = z_input[0], int(z_input[1])

# count = 0

# if x_cold == 'Y' and x_temp >= 37:
#     x_hosp = 'A'
#     count += 1
# elif x_cold == 'N' and x_temp >= 37:
#     x_hosp = 'B'
# elif x_cold == 'Y' and x_temp < 37:
#     x_hosp = 'C'
# else:
#     x_hosp = 'D'

# if y_cold == 'Y' and y_temp >= 37:
#     y_hosp = 'A'
#     count += 1
# elif y_cold == 'N' and y_temp >= 37:
#     y_hosp = 'B'
# elif y_cold == 'Y' and y_temp < 37:
#     y_hosp = 'C'
# else:
#     y_hosp = 'D'

# if z_cold == 'Y' and z_temp >= 37:
#     z_hosp = 'A'
#     count += 1
# elif z_cold == 'N' and z_temp >= 37:
#     z_hosp = 'B'
# elif z_cold == 'Y' and z_temp < 37:
#     z_hosp = 'C'
# else:
#     z_hosp = 'D'

# if count >= 2:
#     print("E")
# else:
#     print("N")


# 난 비전공자가 맞는 듯

# 정답 코드 *** 문제를 풀 때 생각을 좀 하고 풀자

# 변수 선언 및 입력
inp = input().split()
c1, t1 = inp[0], int(inp[1])
inp = input().split()
c2, t2 = inp[0], int(inp[1])
inp = input().split()
c3, t3 = inp[0], int(inp[1])

# A가 2명 이상인지 판단하기
if c1 == 'Y' and t1 >= 37:
    # 첫 번째 사람이 A라면, 남은 두 사람 중 한 사람이라도 A면 됩니다.
    if (c2 == 'Y' and t2 >= 37) or (c3 == 'Y' and t3 >= 37):
        print("E")
    else:
        print("N")
else:
    # 첫 번째 사람이 A가 아니라면, 남은 두 사람 모두 A여야만 합니다.
    if (c2 == 'Y' and t2 >= 37) and (c3 == 'Y' and t3 >= 37):
        print("E")
    else:
        print("N")