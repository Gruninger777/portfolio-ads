#include <stdio.h>

void exibir_array(int array[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

int somar_array(int array[], int tamanho) {
    int soma = 0;

    for (int i = 0; i < tamanho; i++) {
        soma += array[i];
    }

    return soma;
}

int main(void) {
    int valores[] = {10, 20, 30, 40, 50};
    int tamanho = sizeof(valores) / sizeof(valores[0]);

    printf("Valores do array: ");
    exibir_array(valores, tamanho);
    printf("Soma dos valores: %d\n", somar_array(valores, tamanho));

    return 0;
}
