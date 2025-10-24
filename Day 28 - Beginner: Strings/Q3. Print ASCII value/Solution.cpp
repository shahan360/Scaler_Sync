#include<iostream>

using namespace std;

int main()  {
    // YOUR CODE GOES HERE
    // Please take input and print output to standard input/output (stdin/stdout)
    // E.g. 'cin' for input & 'cout' for output
    string str;
    cin >> str;
    
    for (int i = 0; i < str.length(); i++) {
        cout << int(str[i]) << " "; // keep one space even after the last ASCII
    }

    // do NOT print endl or \n here
    return 0;
}