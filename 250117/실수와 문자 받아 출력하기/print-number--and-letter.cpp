// <문제: 실수와 문자 받아 출력하기>
// 문자 c와 실수 a, b를 입력받아 출력하되 실수는 반올림하여 소수 둘째자리까지 출력하는 프로그램

#include <iostream>
#include <string>
using namespace std;

int main() {
    char c;
    double a, b;

    cin >> c >> a >> b;
    
    cout << fixed;
    cout.precision(2);

    cout << c << endl << a << endl << b;
    return 0;
}