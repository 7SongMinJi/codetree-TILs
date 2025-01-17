// <문제: 큰 수에서 빼기>

#include <iostream>
using namespace std;

int main() {
    int a, b;

    cin >> a >> b;

    if (a >= b) {
        cout << a - b;
    }
    else {
        cout << b - a;
    }
    
    return 0;
}