#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
  int participantes, rodadas, teste = 1;
  while(cin >> participantes >> rodadas && participantes != 0){
    int numero_participantes = 0, ordem = 0, acao = 0, posicao;
    list <int> vencedor;
    
    for (int i = 0; i < participantes; i++){
      cin >> posicao;
      vencedor.push_back(posicao);
    }

    for (int i = 0; i < rodadas; i++){ // i = 2
      auto j = vencedor.begin();
      cin >> numero_participantes >> ordem;

      for (int i = 0; i < numero_participantes; i++){
        cin >> acao;
        if (acao != ordem){
          j = vencedor.erase(j);
          j--;
        }
        j++;
      }
    }

    cout << "Teste " << teste++ << endl;
    cout << vencedor.front() << endl << endl;
  }

  
  return 0;
}