#include <iostream>
#include <stack>
using namespace std;

int main(){
  int qtde_casos;
  string caracteres;
  cin >> qtde_casos;

  while (qtde_casos--){
    cin >> caracteres;
    stack <char> expressoes;
    bool ok = true;

    for (char caractere : caracteres){
      if (caractere == '{' || caractere == '[' || caractere == '('){
        expressoes.push(caractere);
      }else{
        if (expressoes.size() > 0 && expressoes.top() == '{' && caractere == '}'){
          expressoes.pop();
        } else if (expressoes.size() > 0 && expressoes.top() == '[' && caractere == ']'){
          expressoes.pop();
        } else if (expressoes.size() > 0 && expressoes.top() == '(' && caractere == ')'){
          expressoes.pop();
        }else{
          ok = false;
          break;
        }
      }
    }

    if (expressoes.size() > 0) ok = false;
    cout << (ok ? "S" : "N") << endl;
  }

  return 0;
}