#include<bits/stdc++.h>
using namespace std;

//Split array into two equal sum sub array
int findSplitIndex(vector<int> &arr, int n) 
{ 
    int leftSum = 0 ; 
    for (int i = 0; i < n; i++) 
    { 
        // add current element to left Sum 
        leftSum += arr[i] ; 
  
        // find sum of rest array elements (rightSum) 
        int rightSum = 0 ; 
        for (int j = i+1 ; j < n ; j++ ) 
            rightSum += arr[j] ; 
  
        // split point index 
        if (leftSum == rightSum) 
            return i+1 ; 
    } 
    // if it is not possible to split array into 
    // two parts 
    return -1; 
} 
  
// Prints two parts after finding split point using 
// findSplitPoint() 
void printSubArray(vector<int> &arr, int n) 
{ 
    int splitPoint = findSplitIndex(arr, n); 
  
    if (splitPoint == -1 || splitPoint == n ) 
    { 
        cout << "Not Possible" <<endl; 
        return; 
    } 
    for (int i = 0; i < n; i++) 
    { 
        if(splitPoint == i) 
            cout << endl; 
        cout << arr[i] << " " ; 
    } 
} 
int main()
{
  vector<int> arr = {1,2,3,4,5,6};
  int n = arr.size();
  printSubArray(arr, n);
  return 0;
}