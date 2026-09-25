/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        vector<ListNode*> data; 
        ListNode* cur = head; 


        while(cur){
            data.push_back(cur);
            cur = cur->next; 
        }


        int l=0;
        int r=data.size()-1; 


        while(l<r){
            data[l]->next=data[r]; 
            l++; 

            if(l==r) break; 

            data[r]->next=data[l];
            r--; 
        }

        data[l]->next=nullptr; 
    }
};
