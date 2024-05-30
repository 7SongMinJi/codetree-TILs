# # 정수를 문자열로 변환하기

# # str() 함수: python에서 정수를 문자열로 변환하기 위해서는 정수를 str() 함수로 감싸주면 됨!
# a = 123
# a = str(123) + '456'
# print(a)
# # >> 123456


# 문제

a, b = map(int, input().split())

aPlusb = str(a + b)
cnt = 0

for elem in aPlusb:
    if elem == '1':
        cnt += 1

print(cnt)


# //