#include <iostream>
#include <bits/stdc++.h>
using namespace std;

double alvo (double x, double y){
  double hipo = (x * x) + (y * y);
  return sqrt(hipo);
}

int pontos (double tiro, long long int circulos[], long long int num_circulos){
  long long int pontuacao = 0;
  long long int ponto = num_circulos;
  for (int i = 0; i < num_circulos; i++){
    if (tiro <= circulos[i]){
      pontuacao += ponto;
      break;
    }
    ponto--;
  }
  return pontuacao;
}

int main() {
  long long int num_circulos, tiros, x, y, pontuacao = 0;;
  double tiro;
  cin >> num_circulos >> tiros;
  long long int circulos[num_circulos];

  for (int i = 0; i < num_circulos; i++){
    cin >> circulos[i];
  }

  for (int i = 0; i < tiros; i++){
    cin >> x >> y;
    tiro = alvo(x, y);
    pontuacao += pontos(tiro, circulos, num_circulos);
  }
  cout << pontuacao << endl;
  return 0;
}