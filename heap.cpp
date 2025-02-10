#include <iostream>
#include <vector>
using namespace std;
void heapify(vector<int> &arr, int n, int i)
{
    int large = i;
    int l = (2 * i) + 1;
    int r = (2 * i) + 2;
    if (l < n && arr[l] > arr[large])
    {
        large = l;
    }
    if (r < n && arr[r] > arr[large])
    {
        large = r;
    }
    if (large != i)
    {
        swap(arr[i], arr[large]);
        heapify(arr, n, large);
    }
}
void heapsort(vector<int> &arr)
{
    int n = arr.size();
    for (int i = n - 1; i >= 0; i--)
    {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}
void disp(vector<int> arr)
{
    for (int i = 0; i < arr.size(); i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}
int main()
{
    vector<int> arr = {3, 2, 4, 1, 5};
    cout << "Original array:" << endl;
    disp(arr);
    int n = arr.size();
    for (int i = (n / 2) - 1; i >= 0; i--)
    {
        heapify(arr, n, i);
    }
    cout << "Heapified array:" << endl;
    disp(arr);
    heapsort(arr);
    cout << "Sorted array: " << endl;
    disp(arr);
}