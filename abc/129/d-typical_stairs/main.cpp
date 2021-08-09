#include <bits/stdc++.h>
using namespace std;
typedef int64_t ll;

int main(){
  ll n, m;
  cin >> n >> m;
  
  vector<ll> a(m, 0);
  for(ll i=0; i < m; i++) {
    cin >> a.at(i);
  }
  
  // 次にスキップする段数を保持
  ll skip = 0;
  if (m > 0) {
    skip = a.at(0);
  	a.erase(a.begin());
  }
  
  // 2つ前まで累計を保持
  vector<ll> tmp(2, 0);
  // 0段目: 1通り
  tmp.at(1) = 1;
  
  ll sum = 0;
  // 1段目からn段目までを計算
  for (ll i=0+1; i < n+1; i++){
    if (i == skip) {
      // たどり着けないので sum = 0;
      sum = 0;
      // 次のスキップ段を保持
      if (a.size() > 0) {
        skip = a.at(0);
        a.erase(a.begin());
      }
        
    } else {
    	sum = (tmp.at(0) + tmp.at(1)) % 1000000007;
    }
    
    tmp.at(0) = tmp.at(1);
  	tmp.at(1) = sum;
  }
  
  cout << sum % 1000000007 << endl;
}
