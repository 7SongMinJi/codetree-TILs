// <문제: 변수 값 복사하기 2>

#include <iostream>
using namespace std;

int main() {
    int a = 5, b = 6, c = 7;
    
    a = b = c;

    cout << a << " " << b << " " << c;
    return 0;
}