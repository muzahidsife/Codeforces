#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int k;
        cin >> k;

        vector<int> shuffled(k); 
        unordered_map<int, int> freq;

        for (int i = 0; i < k; i++) {
            cin >> shuffled[i];
            freq[shuffled[i]]++;
        }

        int n = 1, m = k;
        for (int i = 1; i <= k; i++) {
            if (freq[i] > 0 && freq[i] < m) { 
                n = freq[i];
                m = freq[i];
            }
        }

        cout << n << " " << m << endl; 
    }

    return 0;
}
