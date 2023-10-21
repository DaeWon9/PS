#include <stdio.h>
#include <stdlib.h>

void merge(int **arr, int left, int mid, int right);
void mergeSort(int **arr, int left, int right);

int main() {
    int N;

    scanf("%d", &N);

    int **arr = (int **)malloc(sizeof(int *) * N);
    for (int i = 0; i < N; i++) {
        arr[i] = (int *)malloc(sizeof(int) * 2);
        scanf("%d %d", &arr[i][0], &arr[i][1]);
    }

    mergeSort(arr, 0, N - 1);

    for (int i = 0; i < N; i++) {
        printf("%d %d\n", arr[i][0], arr[i][1]);
    }

    for (int i = 0; i < N; i++) {
        free(arr[i]);
    }
    free(arr);

    return 0;
}

void merge(int **arr, int left, int mid, int right) {
    int i, j, k;
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int **L = (int **)malloc(sizeof(int *) * n1);
    int **R = (int **)malloc(sizeof(int *) * n2);

    for (i = 0; i < n1; i++) {
        L[i] = (int *)malloc(sizeof(int) * 2);
        L[i][0] = arr[left + i][0];
        L[i][1] = arr[left + i][1];
    }
    for (j = 0; j < n2; j++) {
        R[j] = (int *)malloc(sizeof(int) * 2);
        R[j][0] = arr[mid + 1 + j][0];
        R[j][1] = arr[mid + 1 + j][1];
    }

    i = 0;
    j = 0;
    k = left;

    while (i < n1 && j < n2) {
        if (L[i][0] < R[j][0]) {
            arr[k][0] = L[i][0];
            arr[k][1] = L[i][1];
            i++;
        } else if (L[i][0] > R[j][0]) {
            arr[k][0] = R[j][0];
            arr[k][1] = R[j][1];
            j++;
        } else { // same
            if (L[i][1] < R[j][1]) {
                arr[k][0] = L[i][0];
                arr[k][1] = L[i][1];
                i++;
            } else {
                arr[k][0] = R[j][0];
                arr[k][1] = R[j][1];
                j++;
            }
        }
        k++;
    }

    while (i < n1) {
        arr[k][0] = L[i][0];
        arr[k][1] = L[i][1];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k][0] = R[j][0];
        arr[k][1] = R[j][1];
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

void mergeSort(int **arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}
