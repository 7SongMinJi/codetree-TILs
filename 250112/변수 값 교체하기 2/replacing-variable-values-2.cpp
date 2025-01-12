// // <다른 변수로부터 변수 값 변경>
// #include <iostream>
// using namespace std;

// int main() {

//     int a = 5, b = 3;
//     cout << "A is " << a << endl;

//     a = b;
//     cout << "A is " << a << endl;

//     a = 2;
//     cout << "B is " << b;

//     return 0;
// }

// <문제: 변수 값 교체하기 2>

#include <iostream>
using namespace std;

int main() {
    
    int a = 5, b = 3;

    a = b;

    cout << a << endl << b;

    return 0;

}