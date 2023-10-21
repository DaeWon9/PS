#include <stdio.h>
#include <stdlib.h>

void rMergeSort(int arr[], int sortedArray[], int left, int right);
void mergeSort(int arr[], int sortedArray[], int n);
void merge(int arr[], int sortedArray[], int left, int mid, int right);

int main(void)
{
    int N, M;
    scanf("%d %d", &N, &M);
    
    int *A = (int*)malloc(sizeof(int) * N);
    int *B = (int*)malloc(sizeof(int) * M);
    int *mergedArray = (int*)malloc(sizeof(int) * (N + M));
    int *sortedArray = (int*)malloc(sizeof(int) * (N + M));
    
    for (int i = 0; i < N; i++){
        scanf("%d", &A[i]);
    }
    for (int i = 0; i < M; i++){
        scanf("%d", &B[i]);
    }
    
    for (int i = 0; i < N + M; i++){
        if (i < N){
            mergedArray[i] = A[i];
        }
        else{
            mergedArray[i] = B[i - N];
        }
    }
    
    mergeSort(mergedArray, sortedArray, N+M);
    
    for (int i = 0; i < N + M; i++){
        printf("%d ", mergedArray[i]);
    }
    
    return 0;

}

void mergeSort(int arr[], int sortedArray[],  int n) {
    rMergeSort(arr, sortedArray, 0, n - 1);
}

void rMergeSort(int arr[], int sortedArray[], int left, int right) {

    int mid;

    if (left < right) {
        mid = (left + right) / 2;
        rMergeSort(arr, sortedArray, left, mid);
        rMergeSort(arr, sortedArray, mid + 1, right);
        merge(arr, sortedArray, left, mid, right);
    }

}

void merge(int arr[], int sortedArray[], int left, int mid, int right) {

    int i = left;
    int k = left;

    int j = mid + 1;

    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) {
            sortedArray[k++] = arr[i++];
        }
        else {
            sortedArray[k++] = arr[j++];
        }
    }

    while (i <= mid) {
        sortedArray[k++] = arr[i++];
    }

    while (j <= right) {
        sortedArray[k++] = arr[j++];
    }

    for (int t = left; t <= right; t++) {
        arr[t] = sortedArray[t];
    }

}
