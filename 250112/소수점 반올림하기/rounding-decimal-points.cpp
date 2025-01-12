// <문제: 소수점 반올림하기>

#include <iostream>
using namespace std;

int main() {
    double a = 25.352;

    cout << fixed;
    cout.precision(1);

    cout << a;

    return 0;
}