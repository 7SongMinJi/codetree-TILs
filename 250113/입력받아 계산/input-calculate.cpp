// // <입력>

// // C++에서는 cin이라는 함수를 통해 공백 단위로 입력을 받을 수 있음
// // cin 역시 cout과 동일하게, 코드 상단에 cin 함수가 들어있는 iostream 헤더를 포함시켜주어야 함
// // 그렇지 않으면 정의되어있지 않다는 에러 발생
// // cin을 통해 정수 하나를 입력받기

// #include <iostream>
// using namespace std;

// int main() {
    
//     int a;
//     cin >> a;
//     cout << a;

//     return 0;
// }

// <문제: 입력받아 계산>

#include <iostream>
using namespace std;

int main() {
    int a;

    cin >> a;
    cout << a + 2;
    return 0;
}