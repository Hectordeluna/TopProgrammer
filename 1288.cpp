// Example program
#include <iostream>
#include <string>

using namespace std;

int main()
{

    int T;
    int Num;
    cin >> T;
    while (T > 0){

        cin >> Num;

        if(Num % 6 == 0 ){
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }

        T--;
    }



}
