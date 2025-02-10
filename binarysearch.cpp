#include <iostream>
#include <vector>
// #include <algorithm>

using namespace std;

int binarysearch(vector<int> arr, int left, int right, int key)
{
    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        if (arr[mid] == key)
        {
            return mid;
        }
        if (arr[mid] < key)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }
    return -1;
}

int main()
{
    vector<int> arr;
    int n;
    int key;
    cout << "Enter array size: ";
    cin >> n;
    cout << "Enter array elements: \n";
    int x;
    for (int i = 0; i < n; i++)
    {
        cin >> x;
        arr.push_back(x);
    }
    cout << "Enter key : ";
    cin >> key;
    // sort(arr.begin(), arr.end()); // Could be used for sorting, but we won't get the right index, correct index = n-result-1;
    int result = binarysearch(arr, 0, n - 1, key);
    if (result == -1)
    {
        cout << "Element not found!";
    }
    else
    {
        cout << "Element found at index: " << n - result - 1;
    }
}