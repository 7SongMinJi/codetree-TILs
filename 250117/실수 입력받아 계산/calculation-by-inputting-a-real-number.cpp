// <문제: 실수 입력받아 계산>

#include <iostream>
using namespace std;

int main() {
    double a, b;

    cin >> a >> b;

    cout << fixed;
    cout.precision(2);

    cout << a + b;

    return 0;
}