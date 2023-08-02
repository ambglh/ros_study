#include <iostream>

/**
 * @brief 求两个整数的和
 * 
 * @param a 第一个整数
 * @param b 第二个整数
 * @return int 两个整数的和
 */
int add(int a, int b) {
    return a + b;
}

/**
 * @brief Person 类表示一个人，包含姓名和年龄属性
 */
class Person {
public:
    /**
     * @brief 构造一个新的 Person 对象
     * 
     * @param name 姓名
     * @param age 年龄
     */
    Person(const std::string& name, int age) : name_(name), age_(age) {}

    /**
     * @brief 获取姓名
     * 
     * @return const std::string& 姓名
     */
    const std::string& getName() const {
        return name_;
    }

    /**
     * @brief 获取年龄
     * 
     * @return int 年龄
     */
    int getAge() const {
        return age_;
    }

private:
    std::string name_; // 姓名
    int age_;         // 年龄
};

int main() {
    int result = add(3, 5);
    std::cout << "Result: " << result << std::endl;

    Person person("Alice", 30);
    std::cout << "Name: " << person.getName() << ", Age: " << person.getAge() << std::endl;

    return 0;
}
