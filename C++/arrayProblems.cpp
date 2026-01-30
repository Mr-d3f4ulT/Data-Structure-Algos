#include<bits/stdc++.h>
using namespace std;
void swap(int *xp, int *yp)  
{  
    int temp = *xp;  
    *xp = *yp;  
    *yp = temp;  
}  
void printArray(vector<int> &arr, int size) {
  for (int i = 0; i < size; i++) {
    cout << arr[i] << " ";
  }
  cout << endl;
}

int findLargestElement(vector<int> &arr, int n)
{
  int maxEle;
  maxEle = arr[0];
  for (int i = 0; i < n; i++)
  {
    if(maxEle < arr[i])
    {
      maxEle = arr[i];
    }
  }
  cout<<"Largest Element in Array is : "<<maxEle<<endl;
  return maxEle;
  /* 
  //or we can use *max property in C++ STL
  cout<<"Maximun Element in Array is : "<<*max_element(0, n);
  */
}
void findSecondLargestElement(vector<int> &arr, int n)
{
  int largestEle, secondLargestEle;
  largestEle = findLargestElement(arr, n);
  secondLargestEle = -1;
  for (int i = 0; i < n; i++)
  {
    if(arr[i] > secondLargestEle && arr[i] != largestEle)
    {
      secondLargestEle = arr[i];
    }
  }
  cout<<"Second Largest Element is : "<<secondLargestEle<<endl;
}
int findSmallestElement(vector<int> &arr, int n)
{
  int smallest = INT_MAX;
  for (int i = 0; i < arr.size(); ++i) 
  {
    if (arr[i] < smallest) 
    {
        smallest = arr[i];
    }
  }
  cout<<"Smallest Element in Array is : "<<smallest<<endl;
  return smallest;
}
void findSecondSmallestElement(vector<int> &arr, int n)
{
  int smallest = findSmallestElement(arr, n);
    int secondSmallestEle = INT_MAX;
    
    for (int i = 0; i < arr.size(); ++i) 
    {
      if (arr[i] != smallest && arr[i] < secondSmallestEle) 
      {
          secondSmallestEle = arr[i];
      }
    }
  cout<<"Second Smallest Element in Array is : "<<secondSmallestEle<<endl;
}
int main()
{
  vector<int> arr = {1,2,4,5,6,3,8};
  int n = arr.size();
  cout<<"Array : ";
  printArray(arr, n);
  //findLargestElement(arr, n);
  //findSecondLargestElement(arr,n);
  //findSmallestElement(arr, n);
  findSecondSmallestElement(arr, n);
  return 0;
}