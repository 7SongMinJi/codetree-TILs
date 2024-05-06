# # 반복문에서의 continue

# # for, while문 안에서 사용 가능
# # if 조건: continue - 해당 조건이 만족할 경우 continue 아래 코드를 더 이상 실행하지 않고 다시 위로 올라가 그 다음 for loop 실행함

# for i in range(a, b + 1):
#     코드1
#     if 조건:
#         코드2
#         continue
#     코드3

# for i in range(5, 11):
#     코드1
#     if i % 2 == 0:
#         코드2
#         continue
#     코드3

# # i가 6, 8, 10인 경우 코드1, 코드2만 수행됨
# # i가 5, 7 ,9인 경우 코드1, 코드3 수행됨

# a, b = 5, 8
# prod = 1
# for i in range(a, b + 1):
#     print(f"current val is {i}")
#     if i % 2 == 0:
#         print("val is even")
#         continue

#     print("val is odd")
#     prod *= i
# print(prod)


# # ***** Side Note *****

# # 코드가 복잡해질수록 코드가 잘 동작하고 있는지를 코드만으로 판단하기 어려움
# # print를 통해 각각의 순간에 변수의 값이 잘 들어있는지 확인해보기!! "Debugging"

# # "print를 적절한 위치에 넣어 각 위치마다 원하는 변수를 출력하므로서 코드가 예상한대로 올바르게 동작하는 지를 확인하여 틀린 부분을 찾아 고쳐볼 수 있습니다."
# # "문제가 복잡해질수록 debugging 은 굉장히 중요하니 꼭 기억하시기를 바랍니다."


# 문제
n = int(input())
cnt = 0

for i in range(1, n + 1):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        cnt += 1

print(cnt)