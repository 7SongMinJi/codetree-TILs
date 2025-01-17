// // <사칙연산>

// // C++에서 자주 이용되는 사칙연산은 덧셈, 뺄셈, 나눗셈, 곱셈
// // 덧셈, 뺄셈, 곱셈의 경우 +, -, *
// // 나눗셈의 경우에는 몫과 나머지를 잘 구해야 함!

// // 나누기 연산시 몫은 / 연산을 통해, 나머지는 % 연산을 통해 구할 수 있음
// // 만약 5를 2로 나누는 경우처럼 나누어 떨어지지 않는 경우에
// // 나눗셈을 진행하여 그 결과를 실수 값으로 받고 싶은 경우라면
// // 연산이 이루어지는 항들 중 반드시 실수 type이 들어있어야 함

// #include <iostream>
// using namespace std;

// int main() {
    
//     int a = 9, b = 4;

//     cout << a + b << ' ' << a * b << ' ' << a - b << ' ';
//     cout << a / b << ' ' << a % b << ' ' << (double)a / b;

//     return 0;
// }

// // SIDE NOTE 1
// // 연산시 만약 연산이 이루어지는 두 항이 모두 정수형인 int 라면 그 결과는 정수(몫)
// // 따라서 실수로 계산된 결과를 얻고싶다면 꼭 (double)을 이용하여 type을 실수형인 double 로 변경해줘야 gka
// // 정수형 변수, int type 변수인 a 를 실수형 type인 double로 바꾸는 것은 (double)a 와 같이 할 수 있음
// // 다만 두 type이 모두 실수형일 필요는 없고, 실수형과 정수형 간의 연산에서는 결과가 실수형이 나오기 때문에, 두 type중 하나만 실수형으로 바꿔주면 됨

// #include <iostream>
// using namespace std;

// int main() {
//     int a = 9, b = 4;
    
//     cout << (double)a / b << endl;
//     cout << (double) (a / b);

//     return 0;
// }

// // (double) a / b 는 double 로 계산이 되지만,
// // (double) (a / b) 는 a/b가 int (몫 : 2) 로 계산된 후, double 로 type 을 바꿔주었기 때문에 결과값이 2

// // SIDE NOTE 2
// // 사칙연산 계산시 type은 더 큰 범위를 따라가게 되어있기 때문에 (정수 < 실수),
// // 정수와 실수가 만나면 계산결과의 type이 실수가 됨
// double a = 1 + 3.5;
// cout << a;
// // 결과는 4.5

// #include <iostream>
// using namespace std;

// int main() {
//     double a = 3 / 3;
//     int b = 4;
//     cout << a + b;

//     return 0;
// }
// // 결과는 5

// <문제: 간단한 사칙연산>

#include <iostream>
using namespace std;

int main() {
    int a, b;

    cin >> a >> b;
    cout << a + b << endl << a - b << endl << a / b << endl << a % b;
    return 0;
}