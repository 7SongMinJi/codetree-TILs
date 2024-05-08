# # 리스트 push, pop, len

# # 비어있는 리스트
# arr = []
# arr = list()

# # append() 함수: 리스트의 맨 끝에 원소 추가
# arr = [3, 5]
# arr.append(9)
# print(arr) # [3, 5, 9]

# # pop() 함수: 리스트의 맨 뒤에 있는 원소 지우기
# arr = [3, 5, 9]
# arr.pop()
# print(arr) # [3, 5]

# # 짝수인 숫자들만으로 이루어진 리스트 구하기
# given_arr = [1, 3, 2, 5, 4, 6, 8, 1, 10]
# even_arr = list()
# for elem in given_arr:
#     if elem % 2 == 0:
#         even_arr.append(elem)
# print(even_arr)
# # [2, 4, 6, 8, 10]

# # len() 함수: 리스트의 길이를 구해줌. 해당 리스트에 있는 원소의 개수 반환
# print(len[1, 3, 5]) # 3 출력
# print(len[3]) # 1 출력

# # 리스트 안의 숫자들의 합을 구하기
# arr = [1, 2, 2, 5]
# n = len(arr)
# sum_val = 0
# for i in range(n):
#     sum_val += arr[i]
# print(sum_val)

# # len 함수 이용하지 않고 리스트 원소들의 합 구하기
# arr = [1, 2, 2, 5]
# sum_val = 0
# for elem in arr:
#     sum_val += elem
# print(sum_val)

# # slicing 활용해 두 번째 숫자부터 끝까지의 합 구하기 ***
# arr = [1, 2, 2, 5]
# sum_val = 0
# for elem in arr[1:]:
#     sum_val += elem
# print(sum_val)


# 문제
arr = list(map(int, input().split()))

sum_val, cnt = 0, 0

for i in range(len(arr)):
    if arr[i] >= 250:
        break
    else:
        sum_val += arr[i]
        cnt += 1

print(f"{sum_val} {sum_val / cnt:.1f}")