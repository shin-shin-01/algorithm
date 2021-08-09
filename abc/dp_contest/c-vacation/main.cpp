#include <bits/stdc++.h>
using namespace std;
typedef int64_t ll;

// o(n)
// - 地道に計算すると o(2^n)
int main() {
  ll n;
  cin >> n;
  
  // k 回目の時に a, b, c を選んだときの最大得点
  vector<ll> a_dp(n, 0), b_dp(n, 0), c_dp(n, 0);
  cin >> a_dp.at(0) >> b_dp.at(0) >> c_dp.at(0);
  
  // 条件: 2日連続で同じものを選択できない
  // i 回目に X を選択したとき i-1 回目に Y, C を選んだときの最大値 + X の得点
  for(ll i=0+1; i < n; i++){
    ll a, b, c;
    cin >> a >> b >> c;
    a_dp.at(i) = a + max(b_dp.at(i-1), c_dp.at(i-1));
    b_dp.at(i) = b + max(c_dp.at(i-1), a_dp.at(i-1));
    c_dp.at(i) = c + max(a_dp.at(i-1), b_dp.at(i-1));
  }
  
  cout << max({a_dp.at(n-1), b_dp.at(n-1), c_dp.at(n-1)}) << endl;
}
