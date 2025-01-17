// <문제: 입력받아 연산하기>

#include <iostream>
using namespace std;

int main() {
    int a, b;

    cin >> a >> b;

    a += 87;
    b %= 10;

    cout << a << endl << b;
    return 0;
}