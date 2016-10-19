// Example program
#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <string>

using namespace std;

int main()
{

    string Num;
    string Num2;
    long long Total = 1;
    cin >> Num;
    long long n = 0;

    while(Num != "0"){
        Num2 = Num;
        sort(Num2.begin(),Num2.end());
        Num = to_string(stoll(Num) - stoll(Num2));
        n++;
    }

    cout << n << endl;


}
