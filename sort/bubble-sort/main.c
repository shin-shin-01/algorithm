#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap (int *x, int *y){
    int temp;
    
    temp = *x;
    *x = *y;
    *y = temp;
}

void bubbleSort(int array[], int array_size) {
    int i, j;
    
    for (i = 0; i < array_size - 1; i++){
        for (j = array_size - 1; j > i; j--){
            if (array[j] < array[j-1]) { swap(&array[j], &array[j-1]); }
        }
    }
}


int main(void){
    printf("Bubble Sort\n");
    
    srand((unsigned int)time(NULL)); //乱数初期化
    
    int array_size = rand() % 10;
    int array[array_size];
    
    for (int i = 0; i < array_size; i++){
        array[i] = rand() % 30;
    }
    
    bubbleSort(array, array_size);
    
    // Result 表示
    printf("List Size : %d\n", array_size);
    for (int i = 0; i < array_size; i++){ printf("%d ", array[i]); }
    printf("\n");
    
    return 0;
}
