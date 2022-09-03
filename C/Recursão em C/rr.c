#include <stdio.h>
#include <conio.h>
#include <stdlib.h>


double fatorial(int n);
int main(void)
{
  int numero;
  double f;
  
  scanf("%d",&numero);
  
  f = fatorial(numero);
  
  printf("Fatorial de %d = %.0lf",numero,f);
  
  getch();
  return 0;
}


double fatorial(int n)
{
  double fat;
  
  if ( n <= 1 )
    return (1);
  else
  {
    fat = n * fatorial(n - 1);
    return (fat);
  }
}