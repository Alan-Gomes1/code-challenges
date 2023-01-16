#include <iostream>
using namespace std;

int main() {
  int n, m, soma, minhocas = 0;
  cin >> n >> m;
  int fazenda[n][m] = {0};

  for (int i = 0; i < n; i++){
    soma = 0;
    for (int j = 0; j < m; j++){
      cin >> fazenda[i][j];
      soma += fazenda[i][j];
    }
    if (soma > minhocas){
      minhocas = soma;
    }
  }

  for (int i = 0; i < m; i++){
    soma = 0;
    for (int j = 0; j < n; j++){
      soma += fazenda[j][i];
    }
    if (soma > minhocas){
      minhocas = soma;
    }
  }
  cout << minhocas << endl;
  return 0;
}