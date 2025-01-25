#include<bits/stdc++.h>
using namespace std;
int arraySearch(int arr[], int n, int element)
{
  for(int i = 0; i < n; i++)
  {
    if(arr[i] == element)
      return i;
  }
  return -1;
}
int arrayTraversal(int arr[], int n)
{
  for (int i = 0; i < n; i++)
  {
    cout<<arr[i]<<" ";
  }
  return 0;
}
int arrayInsertion(int arr[], int n, int element, int position)
{
  int i;
  for ( i = n-1; i >= position; i--)
    arr[i+1] = arr[i];
  arr[position] = element;
  return 0;
}
int arrayDeletion(int arr[], int n, int element)
{
    int pos = arraySearch(arr, n, element);

    if (pos == -1) 
    {
        cout << "Element not found";
        return n;
    }
    //Deleting Element
    int i;
    for (i = pos; i < n - 1; i++)
        arr[i] = arr[i + 1];
    return n - 1;
}
int main()
{
  cout<<"hello";
  return 0;
}