// <문제: 정사각형의 넓이>

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    cout << n * n;

    if (n < 5) {
        cout << endl << "tiny";
    }

    return 0;
}