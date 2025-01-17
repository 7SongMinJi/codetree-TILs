// <문제: 2개의 정수를 서로 더하기>

#include <iostream>
using namespace std;

int main() {
    int a, b;

    cin >> a >> b;

    a += b;
    b += a;

    cout << a << " " << b;
    return 0;
}