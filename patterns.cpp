#include<bits/stdc++.h>
using namespace std;
void pattern2(int n)
{
    for(int i=1; i<=n; i++)
    {
        for (int j = 1; j < i; j++)
        {
            cout<<"* "; //For Ans2
            cout<<j<<" "; //For Ans3
        }
        cout<<endl;
    }
}
void pattern3(int n)
{
    for(int i=1; i<=n; i++)
    {
        for (int j = 1; j < i; j++)
        {
            cout<<j<<" "; 
        }
        cout<<endl;
    }
}
void pattern7(int n)
{
    for (int i =1; i <= n; i++)  
    {  
        for (int j = 1; j <= n-i-1; j++)  
        {  
            cout<<"  ";   
        }  
        for (int k = 1; k <= ( 2 * i + 1); k++)  
        {  
            cout<<"* "; 
        }  
        for (int j = 1; j <= n-i-1; j++)  
        {  
            cout<<"  ";   
        }  
        cout<<endl;
    }  
}
void pattern8(int n)
{
    int gap = 0, stars = 2 * n - 1;
    for (int i = 0; i < n; i++) {

        for (int j = 0; j < gap; j++) {
            cout << ' ';
        }

        for (int j = gap ; j < gap + stars; j++) {
            cout << '*';
        }

        // End the current row of the pattern.
        cout << '\n';

        gap++;
        stars -= 2;
    }
}
void pattern10(int n)
{
    int i,j;
    for(i =1 ; i<=2*n-1; i++)
    {
        int stars=i;
        if(i>n)
            stars = 2*n-i;
        for(int j=1;j<=stars;j++)
        {
            cout<<"*";
        }
        cout<<endl;
    }
}
void pattern11(int n)
{
    int num = 1;
    for (int i = 0; i < n; i++) {
        int cur = 0;
        for (int j = 1; j <= num; j++) {
            cur = ((i + j) & 1);
            cout << cur << " ";
        }
        cout << '\n';
        num++;
    }
}
void pattern12(int n)
{
    int num = 1, gap = (n - 1) * 2;
    for (int i = 0; i < n; i++) {
        int currentNumber = 1;
        int cur = 0;
        for (int j = 1; j <= num; j++) {
            cout << (currentNumber);
            cout << " ";
            currentNumber++;
        }
        for (int j = 1; j <= gap; j++) {
            cout << " ";            
            cout << " ";
        }
        currentNumber--;
        for (int j = 1; j <= num; j++) {
            cout << currentNumber;
            cout << " ";
            currentNumber--;
        }
        cout << '\n';
        num++;
        gap -= 2;
    }
}
void pattern17(int n)
{
    int i,j,k; 
    for(i=0; i<n; i++)
    {
        for(j=0; j<n-i-1; j++)
        {
            cout<<" ";
        }
        char alpha= 'A';
        int breakpoint = (2*i+1)/2;
        for(k=1; k<=2*i+1; k++)
        {
            cout<<alpha<<" ";
            if(k<=breakpoint) alpha++;
            else alpha--;
        }
        for(j=0; j<n-i-1; j++)
        {
            cout<<" ";
        }
        cout<<endl;
    }
}
void pattern18(int n)
{
    for(int row=0;row<n;row++)
    {
        for(int col = 0; col <= row; col++) {
            
            cout << (char)(n - col - 1 + 'A') << ' ';
        }

        cout<<endl;
    }
}
void pattern19(int n)
{
    int iniS = 0;
    //UPPER HALF
    for(int i=0; i<n; i++)
    {
        //Stars
        for(int k=0; k<n-i; k++)
        {
            cout<<"*";
        }
        //Spaces
        for(int j=0; j<iniS; j++)
        {
            cout<<" ";
        }
        //Stars
        for(int k=0; k<n-i; k++)
        {
            cout<<"*";
        } 
        iniS +=2;
        cout<<endl;
    }
    //LOWER HALF
    iniS = 2*n -2;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=i;j++)
        {
            cout<<"*";
        }
        for(int j=0;j<iniS;j++)
        {
            cout<<" ";
        }
        for(int j=1;j<=i;j++)
        {
            cout<<"*";
        }
        iniS-=2;
        cout<<endl;
    }
}
int main()
{
    int n=3, N=5;
    cout<<"Patterns Problem of Striver's A2Z DSA Course/Sheet"<<endl;
    pattern19(n);
    return 0;
}