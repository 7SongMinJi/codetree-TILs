// // <변수값 동시에 복사>

// // 변수 c에 담겨있는 값을 변수 a, 변수 b에 동시에 복사해주기
// // = 연산을 chain 형식으로 적어주면 가능
// // a = b = c 코드를 통해 오른쪽에서부터 먼저 b에 c 값, a에 b 값을 넣어주면 됨

// #include <iostream>
// using namespace std;

// int main() {
//     int a = 5, b = 3, c = 9;
    
//     a = b = c;
//     cout << "A is " << a << " B is " << b << " C is " << c;

//     return 0;
// }

// // 이런 방식으로 a = b = c = 0 이라는 코드를 통해 a, b, c 값을 동시에 전부 0으로 바꿔줄 수도 있음

// <문제: 변수 값 복사하기>

#include <iostream>
using namespace std;

int main () {
    int a = 1, b = 2, c = 3;

    a = b = c;

    cout << a << " " << b << " " << c;
    return 0;
}