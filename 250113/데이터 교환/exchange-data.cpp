// <문제: 데이터 교환>

#include <iostream>
using namespace std;

int main() {
    int a = 5, b = 6, c = 7;

    int temp1 = a;
    a = c;
    int temp2 = b;
    b = temp1;
    c = temp2;

    cout << a << endl << b << endl << c;
    return 0;

}