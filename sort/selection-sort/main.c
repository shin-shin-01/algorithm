#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap (int *x, int *y){
    int temp;
    
    temp = *x;
    *x = *y;
    *y = temp;
}

void selectionSort(int array[], int array_size){
    int i, j, min;
    
    for (i = 0; i < array_size; i++){
        min = i; // 最小値保存
        for (j = i+1; j < array_size; j++){
            if (array[min] > array[j]){
                min = j;
            }
        }
        swap(&array[i], &array[min]);
    }
}

int main(void){
    printf("Selection Sort\n");
    
    srand((unsigned int)time(NULL)); //乱数初期化
    
    int array_size = rand() % 10;
    int array[array_size];
    
    for (int i = 0; i < array_size; i++){
        array[i] = rand() % 30;
    }
    
    selectionSort(array, array_size);
    
    // Result 表示
    printf("List Size : %d\n", array_size);
    for (int i = 0; i < array_size; i++) { printf("%d ", array[i]); }
    printf("\n");
    
    return 0;
}
