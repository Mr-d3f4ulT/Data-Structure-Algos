#include<bits/stdc++.h>
using namespace std;
//Funciton to Swap Elements
void swap(int *xp, int *yp)  
{  
    int temp = *xp;  
    *xp = *yp;  
    *yp = temp;  
}  
//Function to Print Array
void printArray(int arr[], int size) {
  for (int i = 0; i < size; i++) {
    cout << arr[i] << " ";
  }
  cout << endl;
}
//Function to generate random pivot
int generateRandomPivot(int low, int high) {
    srand(time(NULL));
    return low + rand() % (high - low + 1);
}

//Sorting Functions

int partition (int arr[], int low, int high)
{
  //Algorithm for random pivoting using Lomuto Partitioning
  int pivot = arr[high];
  int i = low - 1;
  for (int j = low; j <= high - 1; j++)
  {
    if (arr[j] <= pivot) 
    {
      ++i;
      swap(arr[i], arr[j]);
    }
  }
  swap(arr[i + 1], arr[high]);  
  return i + 1;
}
void quickSort(int arr[], int low, int high)
{
  if (low < high) 
  {
    /*pi is partitioning index, arr[p] is now at right place */
    int pi = partition(arr, low, high);
    quickSort(arr, low, pi - 1);
    quickSort(arr, pi + 1, high);
  }
}    
void quickSortRandomPivot(int arr[], int low, int high)
{//Quick sort using random Pivot without partitioning
  if(low < high)
  {
    int pivotIndex = generateRandomPivot(low, high);
    int pivotValue = arr[pivotIndex];

    swap(arr[pivotIndex], arr[high]);

    int i = low -1;

    for(int j= low; j< high ; j++)
    {
      if(arr[j] < pivotValue)
      {
        i++;
        swap(arr[i], arr[j]);        
      }
    }
    swap(arr[i+1], arr[high]);

    quickSortRandomPivot(arr, low ,i);
    quickSortRandomPivot(arr, i+2, high);
  }
}

void recursiveInsertionSort(int arr[], int i, int n)
{
  if(i == n) //Base Case
    return;
  int j=i;
  while (j>0 && arr[j-1]>arr[j]) 
  {
    swap(arr[j-1], arr[j]);
    j--;
  }
  recursiveInsertionSort(arr, i+1, n);
}

void recursiveBubbleSort(int arr[], int n)
{
  if(n <= 1) 
    return;
  int count = 0; // One pass of bubble sort. After this pass, the largest element is moved (or bubbled) to end. 
  for(int i = 0; i<n-1; i++)
  {
    if(arr[i] > arr[i+1])
    {
      swap(arr[i], arr[i+1]);
      count++;
    }
  }
  // Check if any recursion happens or not, If any recursion is not happen then return 
  if(count == 0)
    return;
  //Largest element is fixed, now recur for  remaining array
  recursiveBubbleSort(arr, n-1);
}

void merge(int arr[], int left, int mid, int right) {
  int i = left, j = mid + 1, k = left;
  int temp[right + 1];

  while (i <= mid && j <= right) {
    if (arr[i] <= arr[j]) {
      temp[k] = arr[i];
      i++;
    } else {
      temp[k] = arr[j];
      j++;
    }
    k++;
  }

  while (i <= mid) {
    temp[k] = arr[i];
    i++;
    k++;
  }

  while (j <= right) {
    temp[k] = arr[j];
    j++;
    k++;
  }

  for (int i = left; i <= right; i++) {
    arr[i] = temp[i];
  }
}
void mergeSort(int arr[], int left, int right) {
  if (left < right) {
    int mid = (left + right) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
  }
}

void insertionSort(int arr[], int n)
{
  for (int i = 0; i < n; i++) 
  {
    int j = i;
    while (j>0 && arr[j-1] > arr[j])
    {
      swap(arr[j-1], arr[j]);
      j--;
    }
  }
} 

void bubbleSort(int arr[], int size) 
{
  //Time Complexity: O(N2) for the worst and average cases and O(N) for the best case. 
  //Space Complexity: O(1)
  int i, j, didSwap;
  for(i=size-1; i>=0; i--)
  { 
    /*
    Optimized approach (Reducing time complexity for the best case): The best case occurs if the given array is already sorted. We can reduce the time complexity to O(N) by just adding a small check inside the loops. We will check in the first iteration if any swap is taking place. If the array is already sorted no swap will occur and we will break out from the loops. Thus the iteration of the outer loop will be just 1. And our overall time complexity will be O(N).
    */
    didSwap = 0;
    for(j = 0; j<= i-1; j++)
    {
      if(arr[j] > arr[j+1])
      {
        swap(arr[j] , arr[j+1]);
        didSwap = 1;
      }
    }
    if (didSwap == 0) 
    {
        break;
    }
  }
}

void selectionSort(int arr[], int n)
{
  //Time complexity: O(N2), for the best, worst, and average cases.
  //Space Complexity: O(1)
  int i,j,minIndex;
  for (i = 0; i < n-1; i++)
  {
    minIndex = i;
    for (j = i+1; j < n; j++)
    {
      if(arr[j]<arr[minIndex])
        minIndex=j;
    }
    swap(&arr[minIndex], &arr[i]);
  }
}
int main()
{
  int arr[]= {13, 46, 24, 52, 20, 9};
  int n = sizeof(arr) / sizeof(arr[0]);
  cout<<"Array before Sorting : ";
  printArray(arr, n);
  cout<<endl;
  cout<<"Array after Sorting : ";
  //selectionSort(arr,n);
  //bubbleSort(arr, n);
  //insertionSort(arr, n);
  //mergeSort(arr, 0, n-1);
  //recursiveBubbleSort(arr, n);
  //recursiveInsertionSort(arr,0, n);
  //quickSort(arr, 0, n-1);
  printArray(arr, n);
  return 0;
}