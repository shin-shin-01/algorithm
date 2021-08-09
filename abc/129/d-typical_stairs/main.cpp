#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int n, m;
  cin >> n >> m;
  
  // 0で初期化
  vector<long long int> dp(n+1, 0);
  vector<int> safe(n+1, true);
 
  for(int i = 0; i < m; i++){ //壊れている段を記録
    int a;
    cin >> a;
    safe.at(a) = false;
  }
 
  for(int i = 0; i <= n; i++){
    if(safe.at(i)){
      if(i == 0 or i == 1){
        dp.at(i) = 1;
      }
      else{
        dp.at(i) = dp.at(i-2) + dp.at(i-1);
        // オーバーフロー -> 先にあまり計算をしておく
        dp.at(i) %= 1000000007;
      }
    }
  }
  cout << dp.at(n) << endl;
}
