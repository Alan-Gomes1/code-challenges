#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
  int registro, distanciaMax, distancia;
  float x = 0, y = 0;
  char direcao;
  bool afastou = false;

  cin >> registro >> distanciaMax;
  for (int i = 0; i < registro; i++){
    cin >> direcao >> distancia;
    if (direcao == 'N'){
      y += distancia;
    } else if (direcao == 'L'){
      x += distancia;
    } else if (direcao == 'S'){
      y -= distancia;
    } else if (direcao == 'O'){
      x -= distancia;
    }
    
    if (sqrt((x * x) + (y * y)) > distanciaMax){
      afastou = true;
    }
  }

  if (afastou){
    cout << 1 << endl;
  } else {
    cout << 0 << endl;
  }

  return 0;
}