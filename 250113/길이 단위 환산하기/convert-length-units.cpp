// <문제: 길이 단위 환산하기>

#include <iostream>
using namespace std;

int main() {
    double n;

    cin >> n;

    cout << fixed;
    cout.precision(1);

    cout << n * 30.48;
    return 0;
}