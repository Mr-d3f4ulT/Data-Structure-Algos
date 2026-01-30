#include<bits/stdc++.h>
using namespace std;
void integerhashMAP()
{
    int n;
    cin>>n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin>>arr[i];
    }
    //precomputing
    unordered_map<int, int> mpp; //Our first priority will be always to use unordered_map and then map. If unordered_map gives a time limit exceeded error(TLE), we will then use the map
    //In the map data structure, the data type of key can be anything like int, double, pair<int, int>, etc. But for unordered_map the data type is limited to integer, double, string, etc. We cannot have an unordered_map whose key is pair<int, int>.
    for (int i = 0; i < n; i++)
    {
        mpp[arr[i]]++;
    }
    for(auto it : mpp)
    {
        cout<<it.first<<"-->"<<it.second<<endl;
    }
    //fetch
    int q;
    cin>>q;
    while(q--)
    {
        int num;
        cin>>num;
        cout<<mpp[num]<<endl;
    }
    

}
void intergerHashing()
{
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    //precompute 
    int hash[13]= {0};
    for (int i = 0; i < n; i++)
    {
        hash[arr[i]] +=1;
    }
    
    int queries;
    cin>>queries;
    while(queries--)
    {
        int num;
        cin>>num;
        cout<<hash[num]<<endl;
    }
}
void charecterHashing()
{
    //CHARECTER HASHING
    string s;
    cin >> s;

    //precompute:
    int hash[256] = {0};
    for (int i = 0; i < s.size(); i++) {
        hash[s[i]]++;
    }

    int q;
    cin >> q;
    while (q--) {
        char c;
        cin >> c;
        // fetch:
        cout << hash[c] << endl;
    }
}

int main()
{
    integerhashMAP();    
    return 0;
}
