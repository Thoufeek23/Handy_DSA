#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool valid_parantheses(string s)
{
    vector<char> ans;
    int top = -1;
    int f = -1;
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '(')
        {
            ans.push_back(s[i]);
            top++;
        }
        else if (s[i] == '{')
        {
            ans.push_back(s[i]);
            top++;
        }
        else if (s[i] == '[')
        {
            ans.push_back(s[i]);
            top++;
        }
        else if (s[i] == ')')
        {
            if (ans[top] == '(')
            {
                ans.pop_back();
                top--;
            }
            else
            {
                break;
            }
        }
        else if (s[i] == '}')
        {
            if (ans[top] == '{')
            {
                ans.pop_back();
                top--;
            }
            else
            {
                break;
            }
        }
        else if (s[i] == ']')
        {
            if (ans[top] == '[')
            {
                ans.pop_back();
                top--;
            }
            else
            {
                break;
            }
        }
        else
        {
            f = 0;
        }
    }
    if (ans.size() == 0 && f != 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    string s;
    cout << "Input : ";
    cin >> s;
    while (s != "exit")
    {
        if (valid_parantheses(s))
        {
            cout << "Valid Paratheses!" << endl;
        }
        else
        {
            cout << "Not a valid paratheses!" << endl;
        }
        cout << "---------Type 'exit' to quit-------------" << endl;
        cout << "Input : ";
        cin >> s;
    }
}
