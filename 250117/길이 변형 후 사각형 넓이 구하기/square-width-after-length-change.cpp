// // <사칙연산 다른 표현법>
// // += -= *= /= %=

// // C++에서 사칙연산 이용시 보통 동일한 변수에 값의 변화를 주는 경우가 대다수
// // 예를 들어, 변수 a에 현재 들어 있는 값에 5만큼을 더 더해주고 싶은 경우, 다음과 같이 코드 작성이 가능
// a = a + 5;
// //하지만 이러한 경우는 자주 발생하기 때문에 c++에서는 다음과 같은 표현법도 제공함
// a += 5;
// // 이는 곱하기, 나누기, 나머지 등의 모든 연산자에 적용이 가능

// #include <iostream>
// using namespace std;

// int main() {
    
//     int a = 9, b = 4;

//     a = a + 5;
//     cout << a << endl; // 14

//     a -= 5;
//     cout << a << endl; // 9

//     a %= b;
//     cout << a << endl; // 1

//     b *= 3;
//     cout << b << endl; // 12

//     return 0;
// }

// <문제: 길이 변형 후 사각형 넓이 구하기>

#include <iostream>
using namespace std;

int main() {
    int a, b;

    cin >> a >> b;

    a += 8;
    b *= 3;

    cout << a << endl << b << endl << a * b;
    return 0;
}