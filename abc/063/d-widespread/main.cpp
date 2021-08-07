#include <bits/stdc++.h>
using namespace std;
#define ll long long

bool check_destroy(vector<ll> &h, ll n, ll a, ll b, ll k){
  // 全ダメージを与えた後に, 残る体力を計算
  // 残る体力を (a-b) 何回で削れるか計算
  ll cnt = 0;
  for (ll i = 0; i < n; i++){
    ll hp = h.at(i) - (b * k);
    if (hp > 0) {
      // 切り上げ: (x + (y-1)) / y
      cnt += (hp + ((a-b) - 1)) / (a-b);
    }
  }
  
  if (cnt > k) {
    return false;
  } else {
    return true;
  }
}

int main() {
  ll n, a, b;
  cin >> n >> a >> b;
  
  ll max_hp = 0;
  vector<ll> h(n);
  
  for (ll i = 0; i < n; i++){
    cin >> h.at(i);
    // 魔物の最大体力を保存
    if (h.at(i) > max_hp) {
      max_hp = h.at(i);
    }
  }
  
  // 魔物の最大体力の回数攻撃したら必ず倒せる
  ll left = 0, right = max_hp;
  // 二分探索
  while (right - left > 1) {
    ll mid = (left + right) / 2;
    if (check_destroy(h, n, a, b, mid)) {
      right = mid;
    } else {
      left = mid;
    }
  }
  
  cout << right << endl;
}
