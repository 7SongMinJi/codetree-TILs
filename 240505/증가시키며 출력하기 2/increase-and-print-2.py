# # while문

# # for문과 비슷한 기능
# # while문: 항상 조건과 같이 쓰이며, while문 안의 조건을 만족하는 동안 조건문 반복 수행

# while 조건:
#     조건 만족시 수행할 코드

# # for문과 마찬가지로 반복문 내부 범위는 들여쓰기 (indentation) 단위로 파악
# # 그래서 while문 수행 코드로 넣어주려면 반드시 들여쓰기 해야 함

# i = 5 // 반복변수 초기값
# while i <= 10: // 반복 조건
#     print(i) // 조건 만족시 수행할 코드
#     i += 1 // 증감값
# print("Done")

# i = 5
# while i < 7:
#     print(i)
#     print(i * 2)
#     i += 1
# print("Done")
# # 5 10 6 12 Done 출력됨


# 문제
i = 10
while i <= 26:
    print(i, end=" ")
    i += 1