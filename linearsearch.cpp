#include <iostream>
#include <vector>
using namespace std;

int linearsearch(vector<int> arr, int key)
{
    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] == key)
        {
            return i;
        }
    }
    return -1;
}

int main()
{
    cout << "Enter array size: ";
    int n;
    cin >> n;
    cout << "Enter array elements: \n";
    vector<int> arr;
    int a;
    for (int i = 0; i < n; i++)
    {
        cin >> a;
        arr.push_back(a);
    }
    int key;
    cout << "Enter key: ";
    cin >> key;
    int result = linearsearch(arr, key);
    if (result == -1)
    {
        cout << "Element not found!";
    }
    else
    {
        cout << key << " found at index: " << result << endl;
    }
}
