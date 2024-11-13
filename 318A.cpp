#include <iostream>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    int odd_count = (n + 1) / 2;
    if (k <= odd_count) {
        cout << 2 * k - 1 << endl;
    } else {
        int even_index = k - odd_count;
        cout << 2 * even_index << endl;
    }
    return 0;
}
