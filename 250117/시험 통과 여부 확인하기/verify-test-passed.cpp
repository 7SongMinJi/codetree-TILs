// // <if else 조건문>

// // else라는 구문을 이용하면, if 조건에 해당하지 않는 경우에만 특정 코드를 수행하게 만들 수 있음
// if (조건) {
  
//   여기에 조건이 참일 경우에만 수행되는 코드 작성

// }
// else {

//     여기에 조건이 거짓일 경우에만 수행되는 코드 작성

// }

// 이 위치에 있는 코드는 조건과 무관하게 항상 수행됩니다.

// #include <iostream>
// using namespace std;

// int main() {
    
//     int a;
//     cin >> a;

//     if (a > 10) {
//         a += 5;
//     }
//     else {
//         a *= 3;
//     }

//     cout << a;
//     return 0;
// }

// <문제: 시험 통과 여부 확인하기>

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    if (n >= 80) {
        cout << "pass";
    }
    else {
        cout << 80 - n << " more score";
    }

    return 0;
}