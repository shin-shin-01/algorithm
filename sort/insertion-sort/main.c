#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap (int *x, int *y){
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

void insertionSort(int array[], int array_size){
    
    for (int i = 0; i < array_size; i++){
        int left = i - 1;
        while (left >= 0 && array[left] > array[left+1] ){
            swap(&array[left], &array[left+1]);
            left = left - 1;
        }
    }
}

int main(void){
    printf("Insertion Sort\n");
    
    srand((unsigned int)time(NULL)); //乱数初期化
    
    int array_size = rand() % 10;
    int array[array_size];
    
    for (int i = 0; i < array_size; i++){
        array[i] = rand() % 30;
    }
    
    insertionSort(array, array_size);
    
    // Result 表示
    printf("List Size : %d\n", array_size);
    for (int i = 0; i < array_size; i++){ printf("%d ", array[i]); }
    printf("\n");
    
    return 0;
}
