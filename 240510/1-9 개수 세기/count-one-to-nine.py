# Counting 배열

# 주사위를 10번 던져 나온 결과... 각 숫자가 몇 번씩 나왔는지 출력하기

# # 1. 중첩 반복문 이용
# arr = [1, 5, 2, 2, 1, 6, 3, 1, 3, 4]
# for i in range(1, 7):
#     cnt = 0
#     for elem in arr:
#         if elem == i:
#             cnt += 1
#     print(f"숫자 {i} - {cnt}번")

# BUT 만약 몇 번씩 나왔는지 저장을 해야 한다면...
# 처음 상태는 모든 숫자가 0번 나온 상황이므로 전부 0으로 초기화된 크기가 7인 배열이 필요함
# (1부터 6까지를 각각 index로 사용한다고 했을 때)

# # 숫자 별 출현 횟수 1 2 3 4 5 6
# count_arr = [0, 0, 0, 0, 0, 0]
# # 혹은 다음과 같이도 정의 가능
# count_arr = [0] * 7
# # list comprehension을 이용할 수도 있음 *****
# count_arr = [0 for _ in range(7)]

# count_arr = [0] * 7 # 오 이렇게도 되나봐 *****
# # 윗코드: [0]이라는 단일 요소 리스트를 7번 반복하여 새로운 리스트를 만드는 구문
# # 결과적으로 이 코드는 [0, 0, 0, 0, 0, 0, 0]과 같은 리스트를 생성하고, 이 리스트를 count_arr 변수에 할당함
# # 이런 유형의 코드는 보통 특정한 값으로 초기화된 리스트를 생성할 때 사용됨
# # 예를 들어, 어떤 요소의 빈도수를 셀 때 유용하게 쓰일 수 있음
# # 리스트의 각 인덱스는 특정 요소의 빈도수를 저장하는 역할을 하며, 모든 인덱스의 초기 값은 0
# # 특정한 값이나 조건에 따라 각 인덱스의 값을 증가시켜 빈도수를 계산할 수 있음

# count_arr = [0] * 7
# # 개수 세기 *****
# arr = list(map(int, input().split()))
# for elem in arr:
#     count_arr[elem] += 1 # *****
# # 개수 출력
# for i in range(1, 7):
#     cnt = count_arr[i]
#     print(f"숫자 {i} - {cnt}번")


# 정답 코드

n = int(input())
count_arr = [0] * 10
arr = list(map(int, input().split()))

for elem in arr:
    count_arr[elem] += 1

for elem in count_arr[1:]:
    print(elem)