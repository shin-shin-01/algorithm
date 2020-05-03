#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void swap (int *x, int *y){
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}


void shellSort(int array[], int array_size){
    
    int h = array_size / 2;
    
    while(h > 0){
        for (int i = 0; i < array_size; i++){
            
            int here = i;
            
            while(here >= h && array[here-h] > array[here]){
                swap(&array[here-h], &array[here]);
                here = here - h;
            }
        }
        h = h / 2;
    }
}


int main(void){
    printf("Shell Sort\n");
    
    srand((unsigned int)time(NULL)); //乱数初期化
    
    int array_size = rand() % 10;
    int array[array_size];
    
    for (int i = 0; i < array_size; i++){
        array[i] = rand() % 30;
    }
    
    shellSort(array, array_size);
    
    // Result 表示
    printf("List Size : %d\n", array_size);
    for (int i = 0; i < array_size; i++){ printf("%d ", array[i]); }
    printf("\n");
    
    return 0;
}
