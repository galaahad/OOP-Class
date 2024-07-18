#include <iostream>
using namespace std;
// สร้าง Class ชื่อ MathOperations
class Calculator {
public:
    // Class Method สำหรับการบวก
    int add(int a, int b) {
        return a + b;
    }
    // Class Method สำหรับการหาร
    int divide(int a, int b) {
        if (b == 0) {
            cout << "Error: Cannot divide by zero." << endl;
            return 0;
        }
        return a / b;
    }
};

int main() {
    // เรียกใช้ Class Methods โดยตรงโดยไม่ต้องสร้าง Instance
    //cout << "ผลบวก คือ: " << Calculator::add(5, 3) << endl;
    //cout << "ผลหาร คือ: " << Calculator::divide(15, 0) << endl;
    Calculator calc;
    cout << "Addition is " << calc.add(5,3) << endl;
    cout << "Division is " << calc.divide(9,3) << endl;

    return 0;
}
