#include <iostream>
#include <string> // สำหรับการใช้งาน string

using namespace std;

// สร้าง Class ชื่อ Employee
class Employee {
private: 
    string name; // ชื่อพนักงาน
    int age;     // อายุพนักงาน
    double salary; // เงินเดือนพนักงาน

public:
    // Constructor (ตัวสร้างวัตถุ)
    Employee(string n, int a, double s) : name(n), age(a), salary(s) {}

    // Method สำหรับรับค่า name
    string get_name() {
        return name;
    }

    // Method สำหรับรับค่า age
    int get_age() {
        return age;
    }

    // Method สำหรับรับค่า salary
    double get_salary() {
        return salary;
    }

    // Method สำหรับกำหนดค่า salary ใหม่
    void set_salary(double new_salary) {
        salary = new_salary;
    }
};

int main() {
    // สร้าง Instance ของ Object ชื่อ employee1 จาก Class Employee
    Employee employee1("John Doe", 30, 50000.00); // สร้างวัตถุพร้อมกำหนดค่าเริ่มต้น

    // แสดงค่า Attributes (คุณสมบัติ) ของ employee1
    cout << "Name: " << employee1.get_name() << endl;
    cout << "Age: " << employee1.get_age() << endl;
    cout << "Salary: " << employee1.get_salary() << endl;

    // เปลี่ยนค่า salary ของ employee1
    employee1.set_salary(60000.00);

    // แสดงค่า salary ใหม่
    cout << "\nNew Salary: " << employee1.get_salary() << endl;

    return 0;
}