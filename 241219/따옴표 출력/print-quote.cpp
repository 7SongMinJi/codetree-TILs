// // <문자열에 특수 문자 포함시키기>

// // C++에서 문자열은 "로 표현 가능
// // but, ""라는 큰따옴표 문자를 출력하고자 할 경우 그냥 ""Hello"" 이렇게 하면 에러 발생
// // 왜냐하면 문자열의 양끝이 어딘지 판단 불가능해짐

// // 코드 - 에러 남
// # include <iostream>
// using namespace std;

// int main() {
//     cout << ""Hello"";

//     return 0;
// }

// // 따라서, 문자열에 "를 문자로서 포함시키기 위해서는 해당 문자 앞에 \를 붙여주기
// // 코드 - "\"\"" 이렇게 할 경우 "" 출력됨
// # include <iostream>
// using namespace std;

// int main() {
//     cout << "\"Hello\"";
    
//     return 0;
// }

// // 이렇게 대다수의 언어에서 "와 같은 특수문자에 대해 앞에 \를 붙여주면 이를 문자로 인식함

// 문제 <따옴표 출력>
#include <iostream>
using namespace std;

int main() {
    cout << "He says \"It\'s a really simple sentence\".";

    return 0;
}