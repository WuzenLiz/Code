#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    vector<int> temps(100);
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        cin >> temps[i]; cin.ignore();
    }
    if (n==0) {
        cout << 0 << endl;
        return 0;
    }else{
       // closest to 0
       closest = temps[0];
       for (int i = 0; i < n; i++) {
           if (abs(temps[i]) < abs(closest)) {
               closest = temps[i];
           }else if (abs(temps[i]) == abs(closest)) {
               closest = max(temps[i], closest);
           }
        }
        cout << closest << endl;
    }
}