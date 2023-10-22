#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void merge(char **arr, int left, int mid, int right, int strLen);
void mergeSort(char **arr, int left, int right, int strLen);

int main() {
    char inputChar[1000];
    int strLen = 0;
    char **strs;
    
    scanf("%s", inputChar);
    
    strLen = (int)strlen(inputChar);
    strs = (char**)malloc(sizeof(char*) * strLen);
    
    for (int i = 0; i < strLen; i++){
        strs[i] = (char*)malloc(sizeof(char) * (strLen + 1));
        int j;
        int idx = 0;
        for (j = i; j < strLen; j++){
            strs[i][idx] = inputChar[j];
            idx++;
        }
        strs[i][idx] = '\0';
    }
    
    mergeSort(strs, 0, strLen - 1, strLen);
    
    for (int i = 0; i < strLen; i++){
        printf("%s\n", strs[i]);
    }
    
    for (int i = 0; i < strLen; i++) {
        free(strs[i]);
    }
    free(strs);
}

void merge(char **arr, int left, int mid, int right, int strLen) {
    int i, j, k;
    int n1 = mid - left + 1;
    int n2 = right - mid;

    char **L = (char **)malloc(sizeof(char *) * n1);
    char **R = (char **)malloc(sizeof(char *) * n2);

    for (i = 0; i < n1; i++) {
        L[i] = (char *)malloc(sizeof(char) * (strLen + 1));
        strcpy(L[i], arr[left + i]);
    }
    for (j = 0; j < n2; j++) {
        R[j] = (char *)malloc(sizeof(char) * (strLen + 1));
        strcpy(R[j], arr[mid + 1 + j]);
    }

    i = 0;
    j = 0;
    k = left;

    while (i < n1 && j < n2) {
        if (strcmp(L[i], R[j]) < 0) {
            strcpy(arr[k], L[i]);
            i++;
        } else {
            strcpy(arr[k], R[j]);
            j++;
        }
        k++;
    }

    while (i < n1) {
        strcpy(arr[k], L[i]);
        i++;
        k++;
    }

    while (j < n2) {
        strcpy(arr[k], R[j]);
        j++;
        k++;
    }

    for (i = 0; i < n1; i++) {
        free(L[i]);
    }
    for (j = 0; j < n2; j++) {
        free(R[j]);
    }
    free(L);
    free(R);
}

void mergeSort(char **arr, int left, int right, int strLen) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid, strLen);
        mergeSort(arr, mid + 1, right, strLen);
        merge(arr, left, mid, right, strLen);
    }
}
