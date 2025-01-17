// // <합과 평균>

// // C++에서 합과 평균은 다음과 같이 직접 연산자를 사용하여 구할 수 있음

// #include <iostream>
// using namespace std;

// int main() {

//     int a = 9, b = 4;

//     cout << a + b << ' ' << (double) (a + b) / 2;

//     return 0;

// }

// // SIDE NOTE 1
// // 만약 다음과 같이 코드를 작성할 경우
// int a = 9, b = 4;
// cout << (double) (a + b / 2);
// // 답은 11
// // 사칙연산의 경우 수학에서와 같이, 우선순위가 존재함
// // 따라서 b / 2를 먼저 계산한 뒤, a값을 더해주게 되므로 결과는 11
// // 평균을 구하는 문제였다면, (a + b) / 2를 작성하여 우선순위에 맞게 계산이 되도록 해야 함

// // <문제: 합과 평균>

#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    cout << fixed;
    cout.precision(1);

    cout << a + b << " " << (double)(a + b) / 2;
    return 0;
}

// <정답>

