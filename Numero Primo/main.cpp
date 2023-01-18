#include <iostream>
using namespace std;

int main() {
  int numero, contagem = 0;
  cin >> numero;

  for (int i = 1; i <= numero; i++){
    if (numero % i == 0){
      contagem++;
    }
  }

  if (contagem == 2){
    cout << "sim" << endl;
  } else {
    cout << "nao" << endl;
  }
  
  return 0;
}