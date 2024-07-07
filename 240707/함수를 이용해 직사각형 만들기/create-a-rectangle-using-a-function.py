# # 인자가 2개인 함수

# # 연속하여 별 m개를 출력하는 것을 n번 반복하는 경우
# # n과 m에 따라 n개의 줄에 걸쳐 각 줄에 m개씩 직사각형 모양으로 별을 출력해주는 함수와 같이
# # 가변적인 값이 여러 개 주어졌을 때에 대한 적절한 처리 역시 가능
# def print_rect(n, m):
#     코드 작성

# # 인자의 개수가 2개 이상인 경우 다음과 같이 각 인자들 사이에 ,를 넣어 적어주면 됨
# # 위의 함수에 n = 3, m = 5라는 값을 넣어 실행하기 위해서는 순서대로 print_rect(3, 5)와 같이 적어서 호출해주면 됨
# # 인자가 3개 이상인 함수 역시 마찬가지 방식으로 정의 가능

# # <인자가 여러 개인 함수 정의>
# # n과 m을 받아, n개의 줄에 걸쳐 각 줄에 m개씩 별을 출력하는 함수
# def print_rect(n, m):
#     for _ in range(n):
#         print("*" * m)

# # <인자가 여러 개인 함수 호출>
# def print_rect(n, m):
#     for _ in range(n):
#         print("*" * m)
    
# row_num, col_num = tuple(map(int, input().split()))
# print_rect(row_num, col_num)


# # tuple과 map에 대해서 다시 한번 짚고 넘어가기

# # <<tuple>>

# # <역할과 기능>
# # 불변성: 한 번 생성되면 그 값을 변경할 수 없음 (이 불변성 덕분에 데이터의 무결성 유지 가능)
# # 순서가 있는 데이터 저장: 리스트처럼 순서가 있는 여러 값을 저장할 수 있음
# # 다양한 용도: 함수의 반환 값으로 여러 값을 반환하거나, 여러 변수에 한 번에 값을 할당하는 데 유용함

# # <특징>
# # 소괄호 ()를 사용하여 정의
# # 쉼표 ,로 요소를 구분
# # 리스트와 달리 값이 변경되지 않음

# # <예제>
# # 튜플 생성
# my_tuple = (1, 2, 3)

# # 튜플 요소 접근
# print(my_tuple[0])  # 출력: 1

# # 튜플의 불변성
# # my_tuple[0] = 4  # 에러 발생: 튜플은 불변이기 때문에 값을 변경할 수 없음

# # 여러 값을 반환하는 함수
# def get_coordinates():
#     return (10, 20)

# x, y = get_coordinates()
# print(x, y)  # 출력: 10 20


# # <<map>>

# # <역할과 기능>
# # 키-값 쌍 저장: 딕셔너리는 키와 그에 대응하는 값의 쌍을 저장
# # 빠른 검색: 키를 사용하여 값을 빠르게 검색할 수 있음
# # 유연성: 값을 변경, 추가, 삭제할 수 있음

# # <특징>
# # 중괄호 {}를 사용하여 정의
# # 키와 값은 콜론 :으로 구분하고, 각 키-값 쌍은 쉼표 ,로 구분
# # 키는 고유해야 하며, 값은 중복될 수 있음
# # 키는 불변 타입(예: 문자열, 숫자, 튜플)이어야 함

# # <예제>
# # 딕셔너리 생성
# my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# # 딕셔너리 요소 접근
# print(my_dict["name"])  # 출력: Alice

# # 값 추가 및 변경
# my_dict["age"] = 26
# my_dict["country"] = "USA"

# # 딕셔너리 요소 삭제
# del my_dict["city"]

# print(my_dict)  # 출력: {'name': 'Alice', 'age': 26, 'country': 'USA'}

# # 딕셔너리 순회
# for key, value in my_dict.items():
#     print(key, value)
# # 출력:
# # name Alice
# # age 26
# # country USA


# 문제
def print_rect(n, m):
    for _ in range(n):
        print("1" * m)


n, m = tuple(map(int, input().split()))
print_rect(n,m)