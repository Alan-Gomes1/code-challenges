#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
  cout << fixed << setprecision(1);

  char letra;
  string texto;
  float tamanho = 0, contador = 0, palavras = 1;
  bool ocorrencia = false;

  cin >> letra;
  cin.ignore();
  getline(cin, texto);

  for (int i = 0; i < texto.size(); i++){
    if (texto[i] == letra && ocorrencia == false){
      contador++;
      ocorrencia = true;
    } else if (texto[i] == ' '){
      palavras++;
      ocorrencia = false;
    }
  }

  if (palavras > 1 && contador > 0){
    tamanho = (contador / palavras) * 100;
  } else if (palavras == 1 && contador > 0){
    tamanho = 100.0;
  } else {
    tamanho = 0.0;
  }
  cout << tamanho << endl;
  return 0;
}