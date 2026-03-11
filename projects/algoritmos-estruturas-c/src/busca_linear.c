#include <stdio.h>

int busca_linear(int array[], int tamanho, int valor) {
    for (int i = 0; i < tamanho; i++) {
        if (array[i] == valor) {
            return i;
        }
    }

    return -1;
}

int main(void) {
    int numeros[] = {4, 8, 15, 16, 23, 42};
    int tamanho = sizeof(numeros) / sizeof(numeros[0]);
    int valor_procurado = 16;
    int resultado = busca_linear(numeros, tamanho, valor_procurado);

    printf("Array analisado: ");
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", numeros[i]);
    }

    printf("\nValor procurado: %d\n", valor_procurado);

    if (resultado >= 0) {
        printf("Resultado: valor encontrado na posição %d\n", resultado);
    } else {
        printf("Resultado: valor não encontrado\n");
    }

    return 0;
}
