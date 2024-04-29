
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <locale>
#include <map>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <unordered_set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <utility>
#include <valarray>
#include <vector>
#include <cstring>
#include <unordered_map>
#include <cmath>
#include <array>
#include <cassert>
#include <random>
#include <chrono>

using namespace std;

#define          BIT(i,j)  (((i)>>(j))&1LL)
#define           MASK(i)  (1LL<<(i))
#define            ALL(x)  (x).begin(),(x).end()
#define             SZ(x)  (int)(x).size()
#define                fi  first
#define                se  second
#define                ll  long long
#define                ld  long double
#define                vi  vector<int>
#define               vvi  vector<vi>
#define              vvvi  vector<vvi>
#define               pii  pair<int,int>
#define              vpii  vector<pii>
#define             vvpii  vector<vpii>
#define REPDIS(i,be,en,j)  for(int i = (be); i<=(en); i+=j)
#define     REPD(i,be,en)  for(int i = (be); i>=(en); i--)
#define      REP(i,be,en)  for(int i = (be); i<=(en); i++)
#define              endl  "\n"
#define                MP  make_pair
#define               int  ll

//-----------------------------------------------------------------------------------------------//
int readInt(){
    char c;
    do{ c = getchar(); }while(c!='-' && !isdigit(c));
    bool neg = (c=='-');
    int res = neg?0:c-'0';
    while(isdigit(c=getchar())) res = (res<<3)+(res<<1)+(c-'0');
    return neg?-res:res;
}
//------------------------------------------------------------------------------------------------//
const  ll   LINF = 1e18;
const int    INF = 1e9;
const int    LOG = 20;
const int   MAXN = 5e5+7;
const int      N = 1e2+3;
const int    MOD = 1e9+7;
const int   BASE = 1e5;
const  ld    EPS = 1e-9;
const  ld     PI = acos(-1);
const int OFFSET = 1e3;
//------------------------------------------------------------------------------------------------//
template<typename T1, typename T2> bool mini(T1 &a, T2 b){if(a>b){a=b;return true;}return false;}
template<typename T1, typename T2> bool maxi(T1 &a, T2 b){if(a<b){a=b;return true;}return false;}
template<typename T> T gcd(T a, T b) { while(b) { a %= b; swap(a,b); } return a; }
template<typename T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
//------------------------------------------------------------------------------------------------//

/*
----------------------------------------------------------------
    END OF TEMPLATE
----------------------------------------------------------------
*/

int a[MAXN];

void solve(){
    int n; cin >> n;
    int res = 4;
    for(int i = 1; i<=n; i++) cin >> a[i];
    for(int i = 1; i<=n; i++){
        set<int> s;
        s.insert(i);
        s.insert(a[i]);
        s.insert(a[a[i]]);
        res = min(res,(int)s.size());
    }
    cout << res << endl;
}

signed main(){
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    #define task "test"
    if(fopen(task".inp","r")){
        freopen(task".inp","r",stdin);
        freopen(task".out","w",stdout);
    }

    int test = 1; cin >> test;

    while(test--){
      solve();
    }
    cerr << "\nTime elapsed: " << 1000*clock()/CLOCKS_PER_SEC << "ms\n";
    return 0;
}

/**  /\_/\
 *  (= ._.)
 *  / >TL \>AC
**/

