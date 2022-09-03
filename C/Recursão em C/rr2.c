#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
int sequencia(int n) {
  int x;
  
  if (n == 1) {
    return(1);
  }
  
  if (n == 2) {
    return(1);
  }
  
  x = sequencia(n-1) + sequencia(n-2);
  return(x);
}


int main() {
  int n,i;
  
  printf("Qual a quantidade de termos da sequência ?");
  scanf("%d", &n);
  
  while(n <= 0) {
    printf("Numero incorreto. Qual a quantidade de termos da sequência ?");
    scanf("%d", &n);
  }
  
  for (i = 1; i <= n; i++) {
    printf("%d ", sequencia(i));
  }
  printf("\n");
  return(0);
}