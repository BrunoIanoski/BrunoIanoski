#include <stdio.h>

int main(){
    printf("\n\tHello \"World\"\n\n");

    int x = 2000000000;
    float y = 56.34;
    double z = 26.34326;
    char letra = 'b';
    printf("\n\tO valor de 'x': %i %.2f %.3lf %c \n", x, y, z, letra);
    printf("\nSaida ...: %i\n", x);

    int resultado = 5 / 2;
    float num1 = 9;
    int num2 = 9.99;
    printf("Resultado: %d\n", resultado);

    float num3 = (float) 5 / 2;
    char ch = (char) num1;
    printf("Num3: %.2f\n", num3);

    return 0;
}
