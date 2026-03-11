#include <stdio.h>

void ordenar_crescente(int array[], int tamanho) {
    for (int i = 0; i < tamanho - 1; i++) {
        for (int j = 0; j < tamanho - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                int temporario = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temporario;
            }
        }
    }
}

int main(void) {
    int numeros[] = {9, 3, 7, 1, 5};
    int tamanho = sizeof(numeros) / sizeof(numeros[0]);

    ordenar_crescente(numeros, tamanho);

    printf("Array ordenado em ordem crescente: ");
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", numeros[i]);
    }
    printf("\n");

    return 0;
}
