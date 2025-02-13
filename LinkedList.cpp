#include <iostream>

using namespace std;

struct Node
{
    Node *next;
    int data;
};

class LinkedList
{
    Node *head;

public:
    LinkedList();
    void insertathead(int val);
    void insertatend(int val);
    void insertatindex(int val, int pos);
    void deleteathead();
    void deleteatend();
    void getelementbyindex(int pos);
    void getindexbyelement(int val);
    void print();
};

LinkedList::LinkedList()
{
    head = NULL;
}

void LinkedList::insertathead(int val)
{
    Node *newnode = new Node();
    newnode->next = head;
    newnode->data = val;
    head = newnode;
}

void LinkedList::insertatend(int val)
{
    Node *newnode = new Node();
    newnode->next = NULL;
    newnode->data = val;
    Node *temp = head;
    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    temp->next = newnode;
}

void LinkedList::insertatindex(int val, int pos)
{
    if (pos < 0)
    {
        cout << "Invaid Index" << endl;
        return;
    }
    if (pos == 0)
    {
        insertathead(val);
    }
    Node *newnode = new Node();
    newnode->data = val;
    Node *temp = head;
    for (int i = 0; i < pos - 1; i++)
    {
        temp = temp->next;
    }
    if (!temp)
    {
        cout << "Invalid Index" << endl;
        delete newnode;
        return;
    }
    newnode->next = temp->next;
    temp->next = newnode;
}

void LinkedList::deleteathead()
{
    Node *temp = head->next;
    delete head;
    head = temp;
}

void LinkedList::deleteatend()
{
    if (head == NULL)
    {
        cout << "Empty List" << endl;
        return;
    }
    Node *temp = head;
    while (temp->next->next != NULL)
    {
        temp = temp->next;
    }
    delete temp->next;
    temp->next = NULL;
}

void ::LinkedList::getelementbyindex(int pos)
{
    if (pos < 0)
    {
        cout << "Invalid index" << endl;
        return;
    }
    if (pos == 0)
    {
        cout << head->data << endl;
        return;
    }
    Node *temp = head;
    for (int i = 0; i < pos; i++)
    {
        temp = temp->next;
    }
    if (!temp)
    {
        cout << "Index out of bound" << endl;
        return;
    }
    cout << temp->data << endl;
}

void LinkedList::getindexbyelement(int val)
{
    if (head == NULL)
    {
        cout << "Empty LinkedList" << endl;
        return;
    }
    if (val == head->data)
    {
        cout << "Index: 0" << endl;
        return;
    }
    Node *temp = head;
    int i = 0;
    while (temp != NULL)
    {
        if (temp->data == val)
        {
            cout << val << " found at index " << i << endl;
            return;
        }
        i++;
        temp = temp->next;
    }
}

void LinkedList::print()
{
    Node *temp = head;
    while (temp != NULL)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

int main()
{
    LinkedList LL;
    LL.insertathead(20);
    LL.print();
    LL.insertathead(30);
    LL.print();
    LL.insertathead(40);
    LL.print();
    LL.insertatend(10);
    LL.print();
    LL.insertatindex(30, 2);
    LL.print();
    LL.deleteatend();
    LL.print();
    LL.deleteathead();
    LL.print();
    LL.getelementbyindex(2);
    LL.getindexbyelement(20);
}
