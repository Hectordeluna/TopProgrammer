// Example program
#include <iostream>
#include <string>

using namespace std;

int main()
{

    int T;
    int X1,Y1,X2,Y2;
    int XT,YT;
    cin >> T;
    while (T--){
        
        cin >> X1 >> Y1 >> X2 >> Y2;

        if(X1 > X2){
            XT = X1 - X2;
        } else {
            XT = X2 - X1;
        }

        if(Y1 > Y2){
            YT = Y1 - Y2;
        } else {
            YT = Y2 - Y1;
        }

        cout << XT + YT << endl;

    }



}
