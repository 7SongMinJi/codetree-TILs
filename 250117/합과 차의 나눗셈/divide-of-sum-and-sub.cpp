// <문제: 합과 차의 나눗셈>

#include <iostream>
using namespace std;

int main() {
    int a, b;

    cin >> a >> b;
    
    cout << fixed;
    cout.precision(2);

    cout << (double)(a + b) / (a - b);

    return 0;
}