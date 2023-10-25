#include<stdio.h>
#include<stdlib.h>

typedef struct time{
    int startTime;
    int finishTime;
} TIME;

void rMergeSort(TIME *arr, TIME *sortedArray, int n, int left, int right);
void mergeSort(TIME *arr, TIME *sortedArray, int n);
void merge(TIME *arr, TIME *sortedArray, int left, int mid, int right);

int main() {
    int n;
    TIME * personArr;
    TIME * personSortedArr;
    
    scanf("%d", &n);
    personArr = (TIME *)malloc(sizeof(TIME) * n);
    personSortedArr = (TIME *)malloc(sizeof(TIME) * n);
    
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &personArr[i].startTime, &personArr[i].finishTime);
    }

    mergeSort(personArr, personSortedArr, n);

    int tempStartTime = personSortedArr[0].finishTime;
    int answer = 1;
    
    for (int i = 1 ; i < n; i ++){
        if (personSortedArr[i].startTime >= tempStartTime){
            answer++;
            tempStartTime = personSortedArr[i].finishTime;
        }
    }
    
    printf("%d\n", answer);

    return 0;
}

void mergeSort(TIME *arr, TIME *sortedArray, int n){
    rMergeSort(arr, sortedArray, n,  0, n - 1);
}

void rMergeSort(TIME *arr, TIME *sortedArray, int n, int left, int right){

    int mid;

    if (left < right) {
        mid = (left + right) / 2;
        rMergeSort(arr, sortedArray, n, left, mid);
        rMergeSort(arr, sortedArray, n, mid + 1, right);
        merge(arr, sortedArray, left, mid, right);
    }

}

void merge(TIME *arr, TIME *sortedArray, int left, int mid, int right){

    int i = left;
    int k = left;

    int j = mid + 1;

    while (i <= mid && j <= right) {
        if (arr[i].finishTime < arr[j].finishTime) {
            sortedArray[k++] = arr[i++];
        }
        else if(arr[i].finishTime > arr[j].finishTime) {
            sortedArray[k++] = arr[j++];
        }
        else{ // finishTime 가 같을 때
            if (arr[i].startTime < arr[j].startTime){
                sortedArray[k++] = arr[i++];
            }
            else{
                sortedArray[k++] = arr[j++];
            }
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
