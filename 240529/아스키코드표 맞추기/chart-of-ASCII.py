# # 아스키 코드에 대응되는 문자 (ASCII)

# # 아스키 코드 값을 알고 있을 때, 대응되는 문자를 알아내는 방법: chr() 함수 이용
# # chr() 함수: python에서 chr(65) 코드를 실행하게 되면 'A'를 받게 됨
# # 고로, 연속한 알파벳끼리는 연속한 아스키 코드 값을 갖기 때문에 chr(66)은 'B'가 나옴
# print(chr(65))
# print(chr(66))
# # >> A
# # >> B


# 문제

arr = input().split()

for i in range(len(arr)):
    arr[i] = int(arr[i])
    print(chr(arr[i]), end=" ")