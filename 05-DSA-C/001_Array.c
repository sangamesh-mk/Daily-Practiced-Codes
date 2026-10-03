#include <stdio.h>

int main() {

    // 1D Array
    int Arr[5] = {10, 20, 30, 40, 50};

    for (int i = 0; i < 5; i++) {
        printf("%d\n", Arr[i]);
    }

    /* Output:
       10
       20
       30
       40
       50
    */


    // 2D Array
    int Arr2[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", Arr2[i][j]);
         
        }
           
        printf("\n");
    }
        {
            printf("%d",Arr2[1][1]); // Output: 5
        }

    return 0;
}
/* Output:
1 2 3 
4 5 6 
7 8 9 
*/

