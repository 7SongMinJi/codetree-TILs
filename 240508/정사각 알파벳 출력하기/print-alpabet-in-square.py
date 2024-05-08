# # 아스키 코드 (ASCII 코드)

# # 아스키 코드: 파이썬에서 사용할 수 있는 모든 문자들은 전부 하나의 숫자에 대응됨
# # 알파벳 대문자(A, B, C, ...), 소문자(a, b, c, ...)끼리는 연속한 숫자들로 매칭되어 있음

# # 특정 문자의 아스키 코드 값은 ord()라는 함수를 이용해 알 수 있음
# # A의 아스키 코드 값은 65, a의 아스키 코드 값은 97
# print(ord('A'))

# # 반대로 아스키 코드 값을 알고 있을 때 대응되는 문자를 알아내기 위해선 chr() 함수 이용
# print(chr(65))

# # 특정 문자 다음에 오는 문자 구하기
# x = "A"
# print(ord(x))
# print(ord(x) + 1)
# print(chr(ord(x) + 1))


# 문제

n = int(input())

cnt = ord('A')

for i in range(n):
    for j in range(n):
        print(chr(cnt), end="")
        cnt += 1
    print()