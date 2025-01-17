// <문제: 세 실수의 반올림>

#include <iostream>
using namespace std;

int main() {
    double a, b, c;

    cin >> a >> b >> c;

    cout << fixed;
    cout.precision(3);

    cout << a << endl << b << endl << c;
    return 0;
}