#include <bits/stdc++.h>
using namespace std;
typedef int64_t ll;

void debug_print(vector<vector<ll>> &a) {
  for (int i=0; i < a.size(); i++) {
    cout << i << ": ";
    for (int j=0; j < a.at(i).size(); j++) {
      cout << a.at(i).at(j) << " ";
    } 
    cout << endl;
  }
}

// o(n*w) = 10^7
int main() {
  ll N, W;
  cin >> N >> W;
  
  // N+1: 何も選んでいないときの値を記録
  vector<vector<ll>> dp(N+1, vector<ll>(W+1, 0));
  
  ll w, v;
  for (ll i=0+1; i < N+1; i++) {
    cin >> w >> v;
    for (ll j=0; j < W+1; j++) {
      if ( j >= w ) { // n番目のアイテムが入る余地がある
        dp.at(i).at(j) = max(v+dp.at(i-1).at(j-w), dp.at(i-1).at(j));
      } else {
        dp.at(i).at(j) = dp.at(i-1).at(j);
      }
    }
  }
  
  // debug_print(dp);
  cout << dp.at(N).at(W) << endl;
}
