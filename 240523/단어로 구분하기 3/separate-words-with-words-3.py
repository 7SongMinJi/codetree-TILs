string = input().split()

for elem in string[::-1]:
    print(elem)

# # 아래는 한 번 해본 거~! input()과 input().split()의 차이!!!!!
# string = input()
# print(string)

# for elem in string[::-1]:
#     print(elem)
# # 만약 string = input()으로 할 경우 문자열 전체가 그냥 하나의 string으로 저장되기 때문에
# # 역순으로 출력하면 그냥 문자열이 거꾸로 출력됨