// <문제: 길이 단위 변환하기>
#include <iostream>
using namespace std;

int main() {
    double ft = 9.2, mi = 1.3;

    cout << fixed;
    cout.precision(1);

    cout << ft << "ft = " << ft * 30.48 << "cm" << endl;
    cout << mi << "mi = " << mi * 160934 << "cm";

    return 0;

}