// <문제: 체질량지수>

#include <iostream>
using namespace std;

int main() {
    int h, w;
    double b;

    cin >> h >> w;
    b = 10000 * w / (h * h);
    cout << b;

    if (b >= 25) {
        cout << endl << "Obesity";
    }

    return 0;
}