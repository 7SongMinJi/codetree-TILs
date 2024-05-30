# # 문자열 비교

# # Python에서는 두 문자열이 동일한지 비교할 때 숫자 비교와 마찬가지로 == 연산자를 그대로 사용하면 됨
# print('aba' == 'aba') # -> True
# print('aba' == 'abc') # -> False

# # Python에서 문자열끼리 <, > 연산 역시 가능! 이는 *** 사전순 ***으로 앞선 문자열이 누구인가에 대한 비교!
# # 값이 더 작을수록 사전순으로 앞선다는 것을 의미
# print('aba' < 'bc') # -> True
# print('a' < 'bc') # -> True
# print('bd' < 'bc') # -> False


# 문제

n, A = input().split()
n = int(n)

cnt = 0

for _ in range(n):
    str = input()
    if str == A:
        cnt += 1

print(cnt)