// Example program
#include <iostream>
#include <string>

using namespace std;

int main()
{

    int T;
    int Num;
    cin >> T;
    while (T--){

        cin >> Num;

        if(Num % 6 != 0 ){
            cout << "NO" << endl;
        } else {
            cout << "YES" << endl;
        }


    }



}
