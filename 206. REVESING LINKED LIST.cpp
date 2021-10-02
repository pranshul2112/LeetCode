
#include <iostream>

class node{
public:
    int data;
    node* next;

    node(int val){
        data = val;
        next = NULL;
    }
};


node* reverse_recursive(node* &head){      
    if(head == NULL || head->next == NULL){
        return head;
    }

    node* newhead = reverse_recursive(head->next);
    head->next->next = head;
    head->next = NULL;

    return newhead;
}
