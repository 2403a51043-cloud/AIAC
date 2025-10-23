#include <iostream>
using namespace std;

// Function to calculate factorial using recursion
int factorial(int n) {
    if (n == 0 || n == 1)
        return 1;  // Base case
    else
        return n * factorial(n - 1);  // Recursive case
}

int main() {
    int num;
    cout << "Input: ";
    cin >> num;

    int result = factorial(num);

    cout << "Output: Factorial = " << result << endl;

    return 0;
}
