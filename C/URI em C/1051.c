#include <stdio.h>

int main() {
    float a;
    scanf("%f", &a);
    if (a<=2000.00){
        printf("Isento");
    }
    else if(a<=3000.00){
    printf("%2.f", ((a-2000)*0.08));
    }
    else if (a<= 4500.00){
        printf("%2.f", 1000*0.18+(a-3000)*0.18);
    }
    else{
        printf("%2.f", (1000*0.18)+(1500*0.18)+(a-4500)*0.28);

    

    }

    }

