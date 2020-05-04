#include <stdio.h>
#include <stdlib.h>
#include <time.h>



void swap(int *x, int *y){
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

void quickSort(int array[], int left, int right){

    if ( left >= right ){
        
    }else{
    
        int start_left = left;
        int start_right = right;
        
        int pivot = left;
        left++;
        
        while(left < right){
            while((left < right) && (array[left] < array[pivot])){
                left++;
            }
            while((left < right) && (array[right] >= array[pivot])){
                right--;
            }

            swap(&array[left], &array[right]);
        }
        
        if (array[left] > array[pivot]) { left--; }
        swap(&array[pivot], &array[left]);
        pivot = left;
        
        if (start_left < pivot){
            quickSort(array, start_left, pivot-1);
        }
        if (pivot < start_right){
            quickSort(array, pivot+1, start_right);
        }
    }
}

int main(void){
    printf("Quick Sort\n");
    srand((unsigned int)time(NULL)); //乱数初期化

    int array_size = rand() % 10;
    int array[array_size];

    for (int i = 0; i < array_size; i++) {
        array[i] = rand() % 30;
    }
    
    quickSort(array, 0, array_size-1);
    
    // Result
    printf("List Size : %d\n", array_size);
    for (int i = 0; i < array_size; i ++) { printf("%d ", array[i]); }
    printf("\n");
    
    return 0;
    
}
