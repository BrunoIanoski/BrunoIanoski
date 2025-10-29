#include <stdio.h>
#include <stdlib.h>
#include "libestruturas.h"

void write_text_overwrite() {
    FILE *f = fopen("resultado.txt", "w"); // "w" cria ou sobrescreve
    if (!f) {
        perror("Erro ao abrir arquivo para escrita");
        return;
    }
    fclose(f);
}

/* Adiciona texto no final do arquivo */
void append_text(const char *filename, const char *text) {
    FILE *f = fopen(filename, "a"); // "a" abre para append
    if (!f) {
        perror("Erro ao abrir arquivo para append");
        return;
    }
    fprintf(f, "%s\n", text);
    fclose(f);
}

/* Lê todo o arquivo de texto e imprime na tela */
void read_text(const char *filename) {
    FILE *f = fopen(filename, "r");
    if (!f) {
        perror("Erro ao abrir arquivo para leitura");
        return;
    }

    char buffer[256];
    while (fgets(buffer, sizeof(buffer), f)) {
        printf("%s", buffer); // fgets já traz o '\n' se houver
    }

    if (ferror(f)) {
        perror("Erro durante a leitura");
    }

    fclose(f);
}


int main(int argc, char *argv[]) {
    // verificar mais de um argumento


    if (argc < 2) {
        write_text_overwrite();
    }


    if (strcmp(argv[1], "inserir") == 0) {
    // 1) Acrescentar texto
       inserir(argv[2], argv[3]);
    }

    return 0;
}