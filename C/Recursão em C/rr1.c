#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
int main()
{
int fat, n;
scanf("%d", &n);

for(fat = 1; n > 1; n = n - 1)
fat = fat * n;

printf("\nFatorial = %d", fat);
return 0;
}