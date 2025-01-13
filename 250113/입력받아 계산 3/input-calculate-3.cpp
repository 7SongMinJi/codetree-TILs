// // <2개의 줄에 걸쳐 입력>

// // C++에서는 cin을 통해 입력을 받으면 줄을 바꿔주는 \n 역시 공백과 마찬가지로 입력에서 무시됨
// // 두 줄에 걸쳐 입력을 받는 경우 앞에서 했던 공백을 끼고 입력을 받는 것과 똑같이 입력을 받으면 됨

// #include <iostream>
// using namespace std;

// int main() {
    
//     int a, b;
//     cin >> a >> b;
//     cout << a << " " << b;

//     return 0;
// }


// <문제: 입력받아 계산 3>

#include <iostream>
using namespace std;

int main() {
    int a, b;

    cin >> a >> b;
    
    cout << a * b;
    return 0;
}