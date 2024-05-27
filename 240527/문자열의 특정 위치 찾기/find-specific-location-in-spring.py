# # 특정 문자열이 포함된 위치 구하기

# # 문자열 s에 특정 문자열 'ab'가 어느 위치에 포함되어 있는지 알 수 있는 방법
# # 포함되어 있지 않다면 -1을 출력, 여러 번 나타난다면 가장 앞선 위치를 찾음

# # 논리적으로 접근하면, 각각의 위치에 대해 조사하며 그 중 정확히 'ab'와 일치하는 위치가 있었는지 확인해야 함
# # 이때 주의: for loop을 [0, length - 2]에서만 돌아야 함 ***
# # 비교시에 i + 1 위치의 문자를 조회하기 때문
# s = 'applebanana'
# length = len(s)
# start_idx = -1
# for i in range(length - 1):
#     if s[i] == 'a' and s[i + 1] == 'b':
#         start_idx = i
#         break
# print(start_idx)

# # python: index라는 키워드 제공.
# # index 함수 사용시 주의: 부분 문자열이 없는 경우 ValueError 발생함
# s = 'applebanana'
# print(s.index('bbb'))
# # >> ValueError: substring not found

# # *** index 함수는 반드시 in 키워드와 함께 사용해야 함 ***
# # in으로 미리 부분 문자열이 있는지 확인하고, 있다면 해당 위치를 찾는 식으로 진행
# # 만약 부분 문자열이 여러 개 있다면, 가장 앞선 위치를 반환해줌
# s = 'applebanana'
# if 'ab' in s:
#     print(s.index('ab'))
# else:
#     print(-1)
# # >> 5

# # python: find() 함수 제공
# # find() 함수: 해당 부분 문자열이 없는 경우에는 -1, 있는 경우에는 가장 앞에 나오는 부분 문자열의 위치 반환
# s = 'applebanana'
# print(s.find('bob'))
# # >> -1


# 문제

given_str, target = input().split()

start_idx = given_str.find(target)

if start_idx == -1:
    print("No")
else:
    print(start_idx)