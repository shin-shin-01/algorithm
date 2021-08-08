#include <bits/stdc++.h>
using namespace std;
typedef int64_t ll;

int main(){
  priority_queue<ll, vector<ll>, greater<ll>> que;
  
  ll q;
  cin >> q;
  
  // すべてのボールに x を足すのではなく
  // これから追加するボールから, それまでの累計を引く, その後 足して元の値に戻す
  ll tmp = 0;
  
  for (int i=0; i < q; i++) {
    ll x;
    int num;
    cin >> num;
      
    // 1: x を袋に入れる
    if (num == 1) {
      cin >> x;
      que.push(x - tmp);
    
	// 2: すべてのボールに x をたす
    } else if (num == 2) {
      cin >> x;
      tmp += x; // 足す値を増加

    // 3: 最小値を記録して取り出す
    } else {
      // 最小値取り出し
      ll min_x = que.top();
      que.pop();

      cout << min_x + tmp << endl; // 出力

    }
  }
}
