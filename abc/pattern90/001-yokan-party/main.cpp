#include <bits/stdc++.h>
using namespace std;
#define ll long long

bool score_check(vector<int> &a, int n, int l, int k, int score) {
  // score を達成できるか？
  int last = 0;
  int cnt = 0;
  for (int i = 0; i < n; i++) {
    // 今回切り取る Yokan の長さが score を満たすとき cut
    if (a.at(i) - last >= score) {
      last = a.at(i);
      cnt++;
      if (cnt == k) {
        // 残りの Yokan の長さが score を満たすか？
        if (l - last >= score) {
          return true;
        } else {
          return false;
        }
      }
    }
  }
  return false;
}

int main() {
  int n, l, k;
  cin >> n >> l >> k;
  vector<int> a(n);
  for (int i = 0; i < n; i++) {
    cin >> a.at(i);
  }
  // 達成できるスコアの最大値を二分探索
  int left = 0, right = l;
  while (right - left > 1) {
    int mid = (left + right) / 2;
    if (score_check(a, n, l, k, mid)) {
      left = mid;
    } else {
      right = mid;
    }
  }
  cout << left << endl;
}
