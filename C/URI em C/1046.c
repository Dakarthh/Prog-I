#include <stdio.h>
 
int main() {
    int a;
    int b;
    scanf("%", &a);
    scanf("%d", &b);
     if (a>b){
         printf("O JOGO DUROU %d HORA(S)\n", 24 - (a-b));
     }
     else if (b>a){
         printf("O JOGO DUROU %d HORA(S)\n", b-a);
     }
     else{
         printf("O JOGO DUROU 24 HORA(S)\n");
     }
 
 
    return 0;
}