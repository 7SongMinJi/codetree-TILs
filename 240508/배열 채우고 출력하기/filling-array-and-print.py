# # List 거꾸로 탐색

# arr = list(map(int, input().split()))
# for i in range(len(arr) - 1, -1, -1):
#     print(arr[i], end=" ")

# # List - Slicing

# # slice([ : : ])를 활용하면 일부 범위, 조건에 해당하는 원소들을 가져올 수 있음

# arr[start:end:step]
# # for문과 굉장히 유사하게 동작함
# # start index 시작 - step씩 뛰며 전진 - end index 직전까지

# # 단, 첫 번째 index부터 slicing을 적용하고 싶다면, 첫 번째 start 값은 비워놔도 됨!
# # 단, 마지막 원소까지 slicing을 적용하고 싶다면, 두 번째 end 값은 비워놔도 됨!
# # 단, step이 1인 경우에는 마지막 step 값은 생략이 가능함!

# arr = [1, 2, 3, 4, 5]
# print(arr[1:3:1]) # arr[1]부터 arr[2]까지 step 1
# print(arr[1:3]) # arr[1]부터 arr[2]까지 step 1
# print(arr[:3]) # arr[0]부터 arr[2]까지 step 1
# print(arr[2:]) # arr[2]부터 arr[4]까지 step 1
# print(arr[3:0:-1]) # arr[2]부터 arr[1]까지 step -1씩 감소하면서

# # 전체 원소를 뒤집고 싶다면, start, end를 모두 비우고 step에 -1만 적으면 됨!! ***
# print(arr[::-1])

# arr = list(map(int, input().split()))
# reversed_arr = arr[::-1] # 전체 원소를 거꾸로 뒤집기

# for elem in reversed_arr:
#     print(elem, end=" ")


# 문제

arr = input().split()

reversed_arr = arr[::-1]

for elem in reversed_arr:
    print(elem, end="")