# # for문

# # 반복변수 i, 원하는 범위 [a, b) range 함수 이용 (= a부터 b-1까지), : 붙여주기

# for i in range(a, b):
#     코드 작성
#     이 위치에 i 값이 a부터 b - 1까지 1씩 증가하며 들어옴

# # 여기서도 for문 내부에 대한 범위는 if 조건문처럼 들여쓰기(indentation) 단위로 파악함

# for i in range(5, 11):
#     print(i)
# print("Done")
# # 5 - 10 & Done 출력됨

# for i in range(5, 7):
#     print(i)
#     print(i * 2)
# print("Done")

# # 0부터 n-1까지 for문 수행
# n = int(input())
# for i in range(n):
#     print(i)
# # 0 - n-1까지 출력됨

# # a부터 b까지의 수 사이에 공백을 두고 출력하기

# # 파이썬 - print 함수 end값 기본적으로 \n으로 설정되어 있음

# a, b = 3, 6
# for i in range(a, b + 1):
#     print(i, end=" ")
# # 3 4 5 6


# 문제
for i in range(5, 18):
    print(i, end=" ")