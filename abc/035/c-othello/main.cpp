#include <bits/stdc++.h>
using namespace std;
#define ll long long


int debug_print_array(vector<int> &a) {
  for (int i = 0; i < a.size(); i++) {
    cout << i << ":" << a.at(i) << endl;
  }
}


int main() {
  int n, q;
  cin >> n >> q;
  
  // imos の計算結果
  vector<int> array(n+1, 0);
  
  for (int i=0; i < q; i++) {
    int l, r;
    cin >> l >> r;
    array.at(l-1) += 1;
    array.at(r) -= 1;
  }
  
  // debug_print_array(array);
  
  // これまでの累計とその位置での変化量で結果を出力
  // - これまでの累計
  int tmp = 0;
  for (int j=0; j < n; j++) {
    tmp += array.at(j);
    cout << tmp % 2; // 0 or 1
  }
  cout << endl;
}
