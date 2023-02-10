#include <iostream>
using namespace std;

int main() {
  int qtde;
  long int numero;

  cin >> qtde;
  long int numeros_proibidos[qtde] = {0};

  for (int i = 0; i < qtde; i++){
    cin >> numeros_proibidos[i];
  }

  while (cin >> numero){
    bool verificacao = false;
    for (int i = 0; i < qtde; i++){
      if (numero == numeros_proibidos[i]){
        verificacao = true;
        break;
      }
    }

      if (verificacao){
        cout << "sim" << endl;
      } else {
        cout << "nao" << endl;
      }
  }
  return 0;
}