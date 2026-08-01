#include <stdio.h>

int positionMax(const float notes[], int taille) {
    if (taille <= 0) return -1;
    int posMax = 0;
    for (int i = 1; i < taille; ++i) {
        if (notes[i] > notes[posMax]) posMax = i;
    }
    return posMax;
}

int positionFirstGreater(const float notes[], int taille, float seuil) {
    for (int i = 0; i < taille; ++i) {
        if (notes[i] > seuil) return i;
    }
    return -1;
}

int main(void) {
    float arr[] = {12.5f, 15.0f, 9.0f, 15.0f, 18.25f};
    int n = sizeof(arr)/sizeof(arr[0]);

    int pos = positionMax(arr, n);
    printf("positionMax -> index=%d, value=%.2f\n", pos, pos >= 0 ? arr[pos] : -1.0f);

    int pgt = positionFirstGreater(arr, n, 15.0f);
    printf("positionFirstGreater(>15.0) -> index=%d, value=%s\n", pgt, pgt >= 0 ? "found" : "not found");

    pgt = positionFirstGreater(arr, n, 18.5f);
    printf("positionFirstGreater(>18.5) -> index=%d (expected -1 if none)\n", pgt);

    return 0;
}
