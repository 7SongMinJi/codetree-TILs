// // <실수 입력>

// // 실수 type을 입력받기 위해서는 실수 type인 double 변수를 선언한 후 입력을 받으면 됨

// #include <iostream>
// using namespace std;

// int main() {

//     double a;
//     cin >> a;
//     cout << a + 0.58;

//     return 0;
// }


// <문제: 실수 받아 그대로 출력>

#include <iostream>
using namespace std;

int main() {
    double n;

    cin >> n;

    cout << fixed;
    cout.precision(2);

    cout << n;
}