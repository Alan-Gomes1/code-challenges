#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
  string mensagem;

  getline(cin, mensagem);
  for (int i = 0; i < mensagem.size() - 1; i++){
    if (mensagem[i] == 'p' && mensagem[i+1] != 'p'){
      mensagem[i] = '.'; // Substituo os P's por pontos e exibo os caracteres diferentes de ponto
    } else if (mensagem[i] == 'p' &&  mensagem[i+1] == 'p'){
      mensagem[i+1] = '.';
      i += 1;
    }
  }

  for (int i = 0; i < mensagem.size(); i++){
    if (mensagem[i] != '.'){
      cout << mensagem[i];
    }
  }
  
  return 0;
}