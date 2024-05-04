# if else 조건문

# if 조건에 해당하지 않는 경우 특정 코드 수행하도록

# if 조건:
#     조건이 참일 경우 수행되는 코드 작성
# else:
#     조건이 거짓일 경우에 수행되는 코드 작성
# 이 부분은 조건과 무관하게 항상 수행됨

# a = int(input())

# if a > 10:
#     a += 5
# else:
#     a *= 3
# print(a)


# 문제
x = int(input())

if x >= 80:
    print("pass")
else:
    print(f"{80 - x} more score")