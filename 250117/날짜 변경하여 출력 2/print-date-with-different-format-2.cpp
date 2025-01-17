// // <특정 문자를 사이에 두고 3개 이상의 값을 입력>

// // - 문자를 사이에 두고 3개의 수를 입력받아 출력하는 코드는 다음과 같음
// // - 는 입력받아 쓰일 곳이 없기 때문에, 하나의 문자형 변수에 받아줄 수 있음

// #include <iostream>
// using namespace std;

// int main() {
    
//     int a, b, c;
//     char d;

//     cin >> a >> d >> b >> d >> c;
//     cout << a << endl << b << endl << c;

//     return 0;

// }

// // 마찬가지로 cin.get()을 이용하여 받을 수도 있음

// #include <iostream>
// using namespace std;

// int main() {
//     int a, b, c;

//     cin >> a;
//     cin.get();
//     cin >> b;
//     cin.get();
//     cin >> c;
    
//     cout << a << endl << b << endl << c;
//     return 0;
// }

// // <문제: 날짜 변경하여 출력 2>

#include <iostream>
using namespace std;

int main() {
    int y, m, d;

    cin >> m;
    cin.get();
    cin >> d;
    cin.get();
    cin >> y;

    cout << y << "." << m << "." << d;
    return 0;

}

// <정답>

