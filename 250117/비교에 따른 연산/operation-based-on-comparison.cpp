// <문제: 비교에 따른 연산>

#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    if (a >= b) {
        cout << a * b;
    }
    else {
        cout << b / a;
    }

    return 0;
}