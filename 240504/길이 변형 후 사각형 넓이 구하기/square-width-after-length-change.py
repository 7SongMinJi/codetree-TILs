# # 사칙연산 다른 표현법

# # += -= *= %=

# a, b = 9, 4

# a = a + 5
# print(a)

# a -= 5 # a = a - 5
# print(a)

# a %= b # a = a % b
# print(a)

# b *= 3 # b = b * 3
# print(b)

# # 순서대로 14 9 1 12


# 문제
arr = input().split()

width = int(arr[0])
height = int(arr[1])

width += 8
height *= 3

print(f"{width}\n{height}\n{width * height}")