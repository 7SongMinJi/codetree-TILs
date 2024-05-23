# # Run-Length Encoding: 간단한 비손실 압축 방식, 연속해서 나온 문자와 연속해서 나온 개수로 나타내는 방식
# # 예를 들어, 문자열 A가 aaabbbbcbb인 경우 a가 3번, b가 4번, c가 1번 그리고 b가 2번 나왔으므로 Run-Lengh Encoding을 적용하면 a3b4c1b2가 됨

# A = input()

# arr_alpha = [0 for _ in range(26)]

# for elem in A:
#     x = ord(elem) - ord('a')
#     arr_alpha[x] += 1

# cnt = 0
# for elem in arr_alpha:
#     if elem > 0 and elem < 10:
#         cnt += 2
#     elif elem >= 10:
#       https://contents.codetree.ai/problems/67/images/ff66df3d-9775-4c77-b9b6-42ee40d7b1a4.png$0  cnt += 3

# print(cnt)
# for i in range(26):
#     if arr_alpha[i] > 0:
#         print(f"{chr(i + ord('a'))}{arr_alpha[i]}", end="")

# # // 틀림. 왜냐하면 연속한 문자 출력하는 거라 잘못 풀었음


# 정답 코드 *****

# 변수 선언 및 입력:
A = input()

# 변환
encoded = ""

# 입력의 첫번째 값을 읽고 초기화합니다.
curr_char = A[0]
num_char = 1
for traget_char in A[1:]:
    if traget_char == curr_char:
        # 지금까지의 문자와 같으면 연속된 문자 개수만 추가해 주고 넘어갑니다.
        num_char += 1
    else:
        # 지금까지의 문자와 다르면 새로운 문자로 바꿔줘야 합니다.
        # 지금까지 세어온 curr_char와 num_char를 기록합니다.
        encoded += curr_char
        encoded += str(num_char)

        # curr_char와 num_char를 현재 값으로 초기화합니다.
        curr_char = traget_char
        num_char = 1
    
# 마지막 덩어리에 해당하는 curr_char와 num_char를 기록합니다.
encoded += curr_char
encoded += str(num_char)

print(len(encoded))
print(encoded)