# # 연속부분수열
# n1, n2 = tuple(list(map(int, input().split())))
# arrA = list(map(int, input().split()))
# arrB = list(map(int, input().split()))
# yesOrNo = 0

# # 수열 B가 수열 A의 연속부분수열인지...
# i, j, cnt = 0, 0, 0
# while i < n1 - n2 + 1:
#     if arrA[i] == arrB[j]:
#         while arrA[i + j] == arrB[j]:
#             j += 1
#             cnt += 1
#         if cnt == n2:
#             yesOrNo = 1
#         j, cnt = 0, 0
#     else:
#         i += 1

# if yesOrNo == 1:
#     print("Yes")
# else:
#     print("No")

# // 내가 쓴 코드는 인덱스 초과 오류...라고 함

n1, n2 = tuple(map(int, input().split()))
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))
yesOrNo = 0

# 수열 B가 수열 A의 연속부분수열인지 확인
i = 0
while i <= n1 - n2:  # arrA의 가능한 모든 시작점에서 검사
    if arrA[i] == arrB[0]:  # 첫 요소가 일치할 경우에만 내부 검사 시작
        j, cnt = 0, 0
        while i + j < n1 and j < n2 and arrA[i + j] == arrB[j]:  # arrA와 arrB의 요소가 일치하는 동안 반복
            j += 1
            cnt += 1
        if cnt == n2:  # cnt가 n2와 같다면 모든 요소가 일치함
            yesOrNo = 1
            break  # 일치하는 부분을 찾았으므로 루프 종료
    i += 1

print("Yes" if yesOrNo == 1 else "No")





# # 아래는 GPT 코드...
# n1, n2 = map(int, input().split())
# arrA = list(map(int, input().split()))
# arrB = list(map(int, input().split()))
# yesOrNo = "No"

# # 수열 B가 수열 A의 연속부분수열인지...
# for start in range(n1 - n2 + 1):  # arrA에서 가능한 모든 시작점 검사
#     if arrA[start:start + n2] == arrB:  # arrA의 부분 리스트와 arrB 비교
#         yesOrNo = "Yes"
#         break

# print(yesOrNo)