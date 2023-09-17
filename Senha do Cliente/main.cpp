#include <iostream>
#include <cstring>
using namespace std;

int senha[6][10];
int digito1[20], digito2[20];
int qtd_senhas, teste;

int main() {
  while(cin >> qtd_senhas && qtd_senhas) {
    memset(senha, 1, sizeof(senha));
    for (int i = 1; i <= qtd_senhas; i++) {
      for (char c = 'A'; c <= 'E'; c++) {
        cin >> digito1[c - 'A'] >> digito2[c - 'A'];
      }
      for (int digito_atual = 0; digito_atual < 6; digito_atual++) {
        char caracter;
        cin >> caracter;
        for (int novo_digito = 0; novo_digito <= 9; novo_digito++) {
          if (novo_digito == digito1[caracter - 'A'] || novo_digito == digito2[caracter - 'A']) {
            continue;
          }
          senha[digito_atual][novo_digito] = 0;
        }
      }
    }
    cout << "Teste " << ++teste << endl;
    for (int digito_atual = 0; digito_atual < 6; digito_atual++) {
      for (int numero_digitado = 0; numero_digitado <= 9; numero_digitado++) {
        if (senha[digito_atual][numero_digitado]) {
          cout << numero_digitado << " ";
        }
      }
    }
    cout << endl << endl;
  }
  return 0;
}