// <문제: 합을 복사하기>

#include <iostream>
using namespace std;

int main() {
    int a = 1, b = 2, c = 3;
    
    a = b = c = a + b + c;

    cout << a << " " << b << " " << c;
    return 0;
}