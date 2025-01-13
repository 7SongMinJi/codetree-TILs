// // <두 변수 값을 교환>
// temp = a;
// a = b;
// b = temp;

// #include <iostream>
// using namespace std;

// int main() {
//     int a = 5, b = 3;
//     int temp;

//     temp = a;
//     a = b;
//     b = temp;

//     cout << "A is " << a << " B is " << b;

//     return 0;
// }

// <문제: 변수 값 교체하기 3>
#include <iostream>
using namespace std;

int main() {
    int a = 3, b = 5;
    int temp = 0;

    temp = a;
    a = b;
    b = temp;

    cout << a << endl << b;
    return 0;
}