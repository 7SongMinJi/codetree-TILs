# # 문자를 원소로 갖는 배열

# # APPLE의 각 문자를 원소로 갖는 리스트는 숫자와 마찬가지로 각 원소의 위치에 문자를 적어주는 방식으로 선언하면 됨
# word = ['A', 'P', 'P', 'L', 'E']

# # 리스트 안에 특정 문자가 있는지 확인하고 몇 번째 index에 있는지 알아내 방법

# 1. 몇 번째 index에 있는지를 저장해줄 idx라는 변수 사용
# 이때, index를 구해야 하기 때문에 for loop에서 i를 사용해야 함

word = ['A', 'P', 'P', 'L', 'E']
# 해당 문자를 찾지 못했다면 -1
idx = -1
# 문자 탐색
for i in range(len(word)):
    if word[i] == 'L':
        idx = i
# 문자가 존재하지 않는 경우
if idx == -1:
    print("not exist")
else:
    print(idx)