#include <bits/stdc++.h>
using namespace std;
typedef int64_t ll;

// 1 <= N, M <= 10^5
// 最大値取得 (値を半分にする): O(logN)
// M回繰り返す: O(M * logN)

int main(){
  ll n, m;
  cin >> n >> m;
  priority_queue<ll> que;
  // 答え
  ll sum = 0;
  
  for (int i=0; i < n; i++) {
    ll a;
    cin >> a;
    que.push(a);
    sum += a;
  }
  
  for (int i=0; i < m; i++) {
    // 最大値
    ll max_a = que.top();
    que.pop();
    
    ll discounted_a = max_a / 2;
    // 合計から割引
    sum -= (max_a - discounted_a);
    que.push(discounted_a);
  }
  
  cout << sum << endl;
}
