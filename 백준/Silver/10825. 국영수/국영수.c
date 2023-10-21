#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void merge(int **arr, char **names, int left, int mid, int right) ;
void mergeSort(int **arr, char **names, int left, int right);

int main() {
    int N;
    scanf("%d", &N);
    getchar();
    
    char **names = (char **)malloc(sizeof(char *) * N);
    for (int i = 0; i < N; i++){
        names[i] = (char *)malloc(sizeof(char) * 10); // 이름은 최대 10자리
    }

    int **arr = (int **)malloc(sizeof(int *) * N);
    for (int i = 0; i < N; i++) {
        arr[i] = (int *)malloc(sizeof(int) * 4);
        scanf("%s", names[i]);
        arr[i][0] = i; // user id
        scanf("%d %d %d", &arr[i][1], &arr[i][2], &arr[i][3]);
        getchar();
    }

    mergeSort(arr, names, 0, N - 1);

    for (int i = 0; i < N; i++) {
        printf("%s\n", names[arr[i][0]]);
    }

    for (int i = 0; i < N; i++) {
        free(arr[i]);
        free(names[i]);
    }
    free(arr);
    free(names);

    return 0;
}

void merge(int **arr, char **names, int left, int mid, int right) {
    int i, j, k;
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int **L = (int **)malloc(sizeof(int *) * n1);
    int **R = (int **)malloc(sizeof(int *) * n2);

    for (i = 0; i < n1; i++) {
        L[i] = (int *)malloc(sizeof(int) * 4);
        L[i][0] = arr[left + i][0];
        L[i][1] = arr[left + i][1];
        L[i][2] = arr[left + i][2];
        L[i][3] = arr[left + i][3];
    }
    for (j = 0; j < n2; j++) {
        R[j] = (int *)malloc(sizeof(int) * 4);
        R[j][0] = arr[mid + 1 + j][0];
        R[j][1] = arr[mid + 1 + j][1];
        R[j][2] = arr[mid + 1 + j][2];
        R[j][3] = arr[mid + 1 + j][3];
    }

    i = 0;
    j = 0;
    k = left;

    // index 1 : kor , 2 : eng , 3 : math
    // 국어점수가 감소하는 순서로
    // 국어점수가 같으면 영어점수가 증가하는 순서로
    // 국어랑 영어가 같으면 수학점수가 감소하는 순서로
    // 모두 같으면 이름의 사전순서가 증가하는 순서로
    while (i < n1 && j < n2) {
        if (L[i][1] > R[j][1]) { // 국어점수가 감소하는 순서로
            arr[k][0] = L[i][0];
            arr[k][1] = L[i][1];
            arr[k][2] = L[i][2];
            arr[k][3] = L[i][3];
            i++;
        } else if (L[i][1] < R[j][1]) {
            arr[k][0] = R[j][0];
            arr[k][1] = R[j][1];
            arr[k][2] = R[j][2];
            arr[k][3] = R[j][3];
            j++;
        } else { // 국어점수가 같으면 영어점수가 증가하는 순서로
            if (L[i][2] < R[j][2]) {
                arr[k][0] = L[i][0];
                arr[k][1] = L[i][1];
                arr[k][2] = L[i][2];
                arr[k][3] = L[i][3];
                i++;
            } else if (L[i][2] > R[j][2]) {
                arr[k][0] = R[j][0];
                arr[k][1] = R[j][1];
                arr[k][2] = R[j][2];
                arr[k][3] = R[j][3];
                j++;
            }else { // 국어랑 영어가 같으면 수학점수가 감소하는 순서로
                if (L[i][3] > R[j][3]) {
                    arr[k][0] = L[i][0];
                    arr[k][1] = L[i][1];
                    arr[k][2] = L[i][2];
                    arr[k][3] = L[i][3];
                    i++;
                }else if (L[i][3] < R[j][3]) {
                    arr[k][0] = R[j][0];
                    arr[k][1] = R[j][1];
                    arr[k][2] = R[j][2];
                    arr[k][3] = R[j][3];
                    j++;
                }else {// 모두 같으면 이름의 사전순서가 증가하는 순서로
                    if (strcmp(names[L[i][0]], names[R[j][0]]) < 0){
                        arr[k][0] = L[i][0];
                        arr[k][1] = L[i][1];
                        arr[k][2] = L[i][2];
                        arr[k][3] = L[i][3];
                        i++;
                    }
                    else{
                        arr[k][0] = R[j][0];
                        arr[k][1] = R[j][1];
                        arr[k][2] = R[j][2];
                        arr[k][3] = R[j][3];
                        j++;
                    }
                }
            }
        }
        k++;
    }

    while (i < n1) {
        arr[k][0] = L[i][0];
        arr[k][1] = L[i][1];
        arr[k][2] = L[i][2];
        arr[k][3] = L[i][3];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k][0] = R[j][0];
        arr[k][1] = R[j][1];
        arr[k][2] = R[j][2];
        arr[k][3] = R[j][3];
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

void mergeSort(int **arr, char **names, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, names, left, mid);
        mergeSort(arr, names,mid + 1, right);
        merge(arr, names, left, mid, right);
    }
}
