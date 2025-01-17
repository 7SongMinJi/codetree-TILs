// <문제: 날짜 변경하여 출력>

#include <iostream>
using namespace std;

int main() {
    int y, m, d;

    cin >> y;
    cin.get();
    cin >> m;
    cin.get();
    cin >> d;

    cout << m << "-" << d << "-" << y;
    return 0;
}