#include<bits/stdc++.h>
using namespace std;
void countDigits()
{
    int n=7789;
    int flag=0;
    while(n!=0)
    {
        //int lastdigit= n%10; //to print the digits of n... dont required if asked to just count the digits
        n=n/10;
        flag= flag+1;
    }
    cout<<"Number of Digits in "<<n<<" are:- "<<flag;
    cout<<endl;
}
bool isArmstrongNum(int num)
{
    int k = to_string(num).length();
    int sum=0;
    int digit;
    int n=num;
    if(n<0) return false;
    while(n!= 0)
    {
        digit= n%10;
        sum=sum+ pow(digit, k);
        n=n/10;
    }
    if(sum==num)
        return true;
    else 
        return false;

}
int minJumps(int arr[], int n) //GREEDY ALGORITHM PROBLEM
{
        // Your code here
    if (n <= 1) return 0;
    if(arr[0]==0) return -1;
        
    int jumps = 0;
    int currentEnd = 0;
    int farthest = 0;
    
    for (int i = 0; i < n; ++i) {
        // Update the farthest point that can be reached
        farthest = max(farthest, i + arr[i]);
        
        // If the current index reaches the end of the current range
        if (i == currentEnd) {
            jumps++;
            currentEnd = farthest;
            
            // If currentEnd reaches or exceeds the last index, return the jump count
            if (currentEnd >= n - 1) {
                return jumps;
            }
        }
    }
    
    // If the end is not reachable
    return -1;
}
long long factorialNumbers(int N)
{    long long fact=1;
    long long x=2;
    while(fact<=N)
    {
        cout<<fact<<" ";
        fact=fact * x;
        x++;
    }
}
int reverseArray(int arr[], int n)
{
    int p1=0, p2= n-1;
    while(p1<p2)
    {
        swap(arr[p1], arr[p2]);
        p1++;
        p2--;
    }
    for (int i = 0; i < n; i++) 
    {
        cout << arr[i] << " ";
    }
}
bool stringPalindrome(string s) //LeetCode 125. Valid Palindrome
{
    /*
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.*/
    int left=0;
    int right= s.length()-1;
    while(left<=right)
    {
        if(isalnum(s[left]))   
        {
            left++;
            continue;
        }
        if(isalnum(s[right]))   
        {
            right--;
            continue;
        }
        if(tolower(s[left])!=tolower(s[right]))   
        {
            return false;
        }
        else
        {
            left++;
            right--;
        }
        return true;
    }
}
int fibonacciNum(int n) //Leetcode 509. Fibonacci Number0-
{
    /*
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.
    Given n, calculate F(n).
    */
    if(n==0)return 0;
    int p=1,bp=0;
    for(int i=2;i<n+1;i++)
    {
        int x=p+bp;
        bp=p;
        p=x;
    }
    return p;
}
int main()
{
    cout<<"Some basic programs in C++";
    cout<<endl;
    string s="A man, a plan, a canal: Panama";
    bool ans = stringPalindrome(s);
    cout<<ans;
    return 0;
}