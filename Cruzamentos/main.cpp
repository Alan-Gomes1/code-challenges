#include <iostream>
using namespace std;

int main() {
  int xm, ym, xr, yr, cruzamentos;
  cin >> xm >> ym >> xr >> yr;

  cruzamentos = (xr + yr) - (xm + ym);
  cout << cruzamentos << endl;
  return 0;
}