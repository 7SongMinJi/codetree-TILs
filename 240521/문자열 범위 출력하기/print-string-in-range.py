# # 공백이 포함된 문자열 입력받아 출력하기

# # python3: 공백이 포함된 문자열을 항상 한 줄 단위로 입력을 받음 -> 기존과 동일하게 input() 함수를 이용하면 쉽게 입력 받을 수 있음
# given_input = input()
# print(given_input)

# # 위의 예시처럼 hello world가 입력으로 돌아온 경우라면, 6번째 문자인 given_input[5]를 출력했을 때는 공백이 나오게 됨
# # 또한 given_input 문자열의 길이를 len() 함수를 이용해 구하게 되면, 공백을 포함한 총 길이가 출력됨
# given_input = input()
# print(given_input[5])
# print(len(given_input))
# # 출력
# # >>    (공백)
# # 11


# 문제
given_input = input()
for i in range(2, 10):
    print(given_input[i], end="")