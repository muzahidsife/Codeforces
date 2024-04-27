#include <bits/stdc++.h>
#define len(s) int32_t((s).size())
#define MASK(k)(1LL<<(k))
#define fi first
#define se second
#define int long long

using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
const int MX = 300005;

int n, m, k, q;
int a[MX];
int b[MX];
string s, t;

void solve(){
    cin >> n >> k;
    for(int i=1; i<=n; i++) cin >> a[i];
    sort(a+1, a+1+n);
    a[n+1] = -1;
    int mx = 0;
    for(int i=1, cnt=0; i<=n; i++){
        if(a[i] != a[i+1]){
            cnt++;
            mx = max(mx, cnt);
            cnt = 0;
        }
        else cnt++;
    }
    if(mx < k){
        cout << n << endl;
        return;
    }
    else cout <<min(n, k-1) << endl;
}

int32_t main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int q;
    cin >> q;
    while(q--){
        solve();
    }

    return 0;
}
