// // <소수점 맞춰 출력하기>
// #include <iostream>
// using namespace std;

// int main() {
    
//     cout << fixed;

//     double a = 33.567268;

//     cout.precision(4);
//     cout << a << endl;

//     cout.precision(2);
//     cout << a << endl;

//     return 0;
// }

// <문제: 달에서 무게 구하기>
#include <iostream>
using namespace std;

int main() {
    int a = 13;
    double b = 0.165;

    cout << fixed;

    cout.precision(6);

    cout << a << " * " << b << " = " << a * b;

    return 0;
}