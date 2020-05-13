#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 作業領域確保
#define MAX_DATA 10
int temp[MAX_DATA];

void mergeSort(int array[], int left, int right){
    int mid, i, j, k;
    
    if (left >= right){
        return;
    }
    
    mid = (left + right) / 2;
    mergeSort(array, left, mid);
    mergeSort(array, mid+1, right);
    
    for (i = left; i <= mid; i++){
        temp[i] = array[i];
    }
    // 逆順
    for (i = mid+1, j = right; i <= right; i++, j--){
        temp[i] = array[j];
    }
    
    i = left;
    j = right;
    
    for (k = left; k <= right; k++) {
        if (temp[i] < temp[j]){
            array[k] = temp[i++];
        }else{
            array[k] = temp[j--];
        }
    }
    return;
}


int main(void){
    printf("Merge Sort\n");
    srand((unsigned int)time(NULL));
    
    int array_size = rand() % 10;
    int array[array_size];
    
    for (int i = 0; i < array_size; i++){
        array[i] = rand() % 30;
    }
    
    mergeSort(array, 0, array_size-1);
    
    // Result
    printf("List Size : %d\n", array_size);
    for (int i = 0; i < array_size; i++) { printf("%d ", array[i]); }
    printf("\n");
    
    return 0;
}
