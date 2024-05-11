# 리스트에 특정 문자가 몇 번 들어있는지 개수 세기

# 1. cnt라는 변수 사용! 0으로 초기화
# word = ['A', 'P', 'P', 'L', 'E']
# cnt = 0
# for char in word:
#     if char == 'P':
#         cnt += 1
# print(cnt)

# # 2. count() 함수: 리스트에 내장되어 있는 함수. 배열 내의 특정 값 개수 세서 return하나봐
# word = ['A', 'P', 'P', 'L', 'E']
# cnt = word.count('P')
# print(cnt)


# 문제
n, m = tuple(list(map(int, input().split())))
arr = list(map(int, input().split()))
cnt = 0

for elem in arr:
    if elem == m:
        cnt += 1

print(cnt)

# // 아 처음에는 if m in arr: 하면 cnt++ 했는데 생각해보니까 그럼 계속 있으니까 10번 출력됨