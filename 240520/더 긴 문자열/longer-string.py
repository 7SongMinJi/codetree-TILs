first_word, second_word = input().split()

if len(first_word) > len(second_word):
    print(first_word, len(first_word))
elif len(first_word) < len(second_word):
    print(second_word, len(second_word))
else:
    print("same")

# //공백 있는 문자열 - 위와 같이 input().split()만 해주면 자동으로 split돼서 초기화됨!

# 정답 코드