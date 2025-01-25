#include<bits/stdc++.h>
using namespace std;
void explainStack()
{
    stack<int> stk;
    stk.push(21);// The values pushed in the stack should be of the same data which is written during declaration of stack
    stk.push(22);
    stk.push(24);
    stk.push(25);
    int num=0;
    stk.push(num);
    stk.pop();
    stk.pop();
    stk.pop();

    while (!stk.empty()) {
        cout << stk.top() <<" ";
        stk.pop();
    }
    stack <int> st1,st2;
    st1.swap(st2);
}
void explainQueue()
{
    queue<int> g;
    g.push(10);
    g.push(20);
    g.push(30);
    g.emplace(40);
    g.emplace(50);
    
    cout << "\ng.size() : " << g.size(); //5
    cout << "\ng.front() : " << g.front(); //10
    cout << "\ng.back() : " << g.back(); //50
    cout <<'\n';
    g.pop(); //10 popped
    cout<<g.front()<<endl;
    cout <<"The queue is :- ";
    while (!g.empty()) 
    {
        cout<< g.front()<<'\t' ;
        g.pop();
    }
    cout <<'\n';
}
void explainPriorityQueue()
{
    priority_queue<int> pq; //Maximum Heap
    pq.emplace(1); // {1}
    pq.push(2);  // {2,1} 
    pq.push(3);  // {3,2,1}
    pq.push(4);  // {4,3,2,1}
    pq.push(5);  // {5,4,3,2,1}
    pq.push(6);  // {6,5,4,3,2,1}
    pq.push(9);  // {9,6,5,4,3,2,1}

    cout<<pq.top()<<endl; //prints 9;
    pq.pop(); // pops 9
    cout<<pq.top()<<endl; //prints 6;

    //Size and swap functions are same as stack and queue

    //MINIMUM HEAP FOR PRIORITY QUEUE
    //priority queue that stores minimum element at the top
    priority_queue <int, vector<int>, greater<int>> prq;
    prq.emplace(1); // {1}
    prq.push(2);  // {1,2} 
    prq.push(3);  // {1,2,3} 
    prq.push(4);  // {1,2,3,4} 
    cout<<prq.top()<<endl; //prints 1;
}
void explainSet()
{
    set<int> st;
    st.insert(1);   //{1} takes O(logn)
    st.emplace(2);  //{1,2}
    st.insert(3);   //{1,2,3}
    st.insert(5);   //{1,2,3,5}
    st.insert(4);   //{1,2,3,4,5}

    /* begin(), end(), rbegin(), rend(), size(), swap() are same as above*/
    //{1,2,3,4,5}
    auto it = st.find(2); // returns an iterator pointing to 2
    auto it = st.find(6); // returns an iterator pointing to position of (last element +1) i.e end

    st.erase(4); // erase 4 and takes O(logn) time
    auto itr = st.find(3);
    st.erase(itr); // erase 3 and takes O(1) time
    auto it1 = st.find(2);
    auto it2 = st.find(4);
    st.erase(it1, it2); // erase 2,3 from set not 4 beacause erase deletes start, end-1 element
    int cnt = st.count(1);
}
void explainMultiSet()
{
    multiset<int> mst; //Only obeys sorted property of set not unique
    mst.insert(1);  //{1} 
    mst.insert(1);  //{1,1}
    mst.insert(2);  //{1,1,2}
    mst.insert(3);  //{1,1,2,3}
    mst.insert(5);  //{1,1,2,3,5}
    mst.insert(4);  //{1,1,2,3,4,5}
    mst.insert(4);  //{1,1,2,3,4,,45}

    mst.erase(1); //All 1's are erased
    mst.erase(mst.find(4)); //only one 4 is erased
    mst.erase(mst.find(1), mst.find(3)); //1,1,2 are erased
    //rest all functions same as set
}
void explainUnorderedSet()
{
    /*
    it stores elements uniquely and not in any sorted manner
    lower_bound and upper_bound funciton doesn't work, rest all function
    are same. it has a better complexity than set, except in some cases where collision occurs.
    */
    unordered_set < int > s;
    for (int i = 1; i <= 10; i++) 
    {
        s.insert(i);
    }

    cout << "Elements present in the unordered set: ";
    for (auto it = s.begin(); it != s.end(); it++) 
    {
        cout << * it << " ";
    }
    cout << endl;
    int n = 2;
    if (s.find(2) != s.end())
        cout << n << " is present in unordered set" << endl;

    s.erase(s.begin());
    cout << "Elements after deleting the first element: ";
    for (auto it = s.begin(); it != s.end(); it++) 
    {
        cout << * it << " ";
    }
    cout << endl;

    cout << "The size of the unordered set is: " << s.size() << endl;

    if (s.empty() == false)
        cout << "The unordered set is not empty " << endl;
    else
        cout << "The unordered set is empty" << endl;
    s.clear();
    cout << "Size of the unordered set after clearing all the elements: " << s.size();
}
void explainMap()
{
    //MAP STORES KEYS IN UNIQUE AND SORTED ORDER
    /*
    map<int, int> mp; where first int is key and second int is value
    map<int, pair<int,int>> mp1; key is an integer and value is a pair of 2 integers
    map<pair<int,int>,int> mp2; key is a pair of 2 integers and value is an integer.
    */
    map<int, int> mp;
    map<int, pair<int,int>> mp;
    map<pair<int,int>,int> mp2;
    mp[1]= 2; //Key= 1 and value is 2 i.e {1,2}
    mp.insert({3,4}); //Key= 3 and value is 4 i.e {3,4}
    mp2[{2,3}]= 10;

    //Travversing a map
    for(auto it : mp)
    {
        cout<<it.first<<" "<<it.second<<endl;
    }

    cout<<mp[1]; //prints 2;
    cout<<mp[5]; //prints null or 0
    
    //LOWER BOUND AND UPPER BOUND
    auto it = mp.lower_bound(1);
    auto it = mp.upper_bound(4);
    //rest functions same as set
}
void explainMultiMap()
{
    //same as map but stores multiple keys with same value in sorted order
}
void explainUnorderedMap()
{
    //same as unordered set but store key in uniquely in unsorted manner
}
bool comp(pair<int, int> p1, pair<int, int> p2)
{
    if(p1.second<p2.second) return true;
    if(p1.second>p2.second) return false;
    //if both above conditions are false then second element of both pairs are same
    if(p1.first>p2.first) return true;
    return false;
}
void explainExtra()
{
    int a[5]= {1,4,5,2,3};
    //sort(a,a+n); a is starting index and a+n end index for an array a
    //sort(v.being(),v.end()); for vector v
    sort(a,a+4);
    //sorting in descending order
    //sort(a,a+4,greater<int>);
    pair<int, int> arr[]= {{1,3},{2,1},{4,1}};
    sort(a,a+3,comp); //{{4,1},{2,1},{1,3}}

    int num=7;
    int cnt= __builtin_popcount(num); //returns 3 as 7 has 3 1-bit in its binary code i.e 111
    long long num1 = 123145584235;
    int cnt= __builtin_popcountll(num);

    //to print all permuations of a string
    string s= "123";
    do
    {
        cout<<s<<endl;
    } while (next_permutation(s.begin(), s.end()));
    
    /*
    to print maximum element in given array
    int maxEle =  max_element(a,a+n); --> gives address of that element
    int maxEle = *max_element(a,a+n); --> gives element
    */
}
int main()
{
    cout<<"Containers and Iterators in C++ STL";
    explainExtra();
    return 0;
}