// // <공백을 사이에 두고 입력>

// // 공백을 사이에 두고 두 개의 수를 입력받고 싶다면
// // cin을 이용해 두 개의 정수형 변수에 입력을 받아주면 됨
// // cin은 공백 단위로 입력을 받아줌! 그래서 공백을 무시한 채 두 개의 숫자만을 입력받을 수 있음

// #include <iostream>
// using namespace std;

// int main() {

//     int a, b;
    
//     cin >> a >> b;

//     cout << a << " " << b;
//     return 0;
// }

// // 두 개의 문자를 공백을 사이에 두고 받는 것 역시 문자형 변수를 이용해 다음과 같이 할 수 있음

// #include <iostream>
// using namespace std;

// int main() {
//     char a, b;
//     cin >> a >> b;
//     cout << a << " " << b;

//     return 0;
// }


// <문제: 입력받아 계산 2>

#include <iostream>
using namespace std;

int main() {

    int a, b;
    cin >> a >> b;

    cout << a * b;
    return 0;
}