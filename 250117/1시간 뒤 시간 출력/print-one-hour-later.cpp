// // <특정 문자를 사이에 두고 2개의 값을 입력>
// // cin.get()

// // 두 수가 공백이 아닌 특정 문자를 사이에 두고 입력으로 들어오는 경우,
// // cin을 이용해 그 문자를 문자형 변수에 입력받아 무시하고 두 개의 수를 받을 수 있음

// #include <iostream>
// using namespace std;

// int main() {

//     int a, b;
//     char c;

//     cin >> a >> c >> b;
//     cout << a << endl << b;

//     return 0;
// }

// // 이때 중간 문자를 무시하는 것을 새로운 변수를 선언하지 않고 cin.get()을 이용하여 해결 가능

// #include <iostream>
// using namespace std;

// int main() {
    
//     int a, b;
    
//     cin >> a;
//     cin.get();
//     cin >> b;
//     cout << a << endl << b;

//     return 0;
// }

// // <cin.get()>

// // <iostream>에 존재
// // 표준 입력 버퍼에서 문자를 하나만 가져옴
// // 공백, 개행 문자 포함
// // 문자만 입력 받음

// <문제: 1시간 뒤 시간 출력>

#include <iostream>
using namespace std;

int main() {
    int h, m;

    cin >> h;
    cin.get();
    cin >> m;

    cout << h + 1 << ":" << m;
    return 0;
}