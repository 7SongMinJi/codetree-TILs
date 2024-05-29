# # 문자열을 정수로 변환하기

# # int() 함수: python에서 문자열을 정수로 변환하기 위해서는 문자열을 int() 함수로 감싸주면 됨
# a = '123'
# a = int(a) + 1
# print(a)
# # >> 124


# 문제

A, B = input().split()

AB = A + B
BA = B + A

print(int(AB) + int(BA))