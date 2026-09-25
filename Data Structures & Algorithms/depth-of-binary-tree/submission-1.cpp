/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:

    int depth(TreeNode* root) {
        if (root == nullptr)
            return 0;

        TreeNode* l = root->left;
        TreeNode* r = root->right;

        return 1 + max(depth(l), depth(r));
    }

    int maxDepth(TreeNode* root) {
        return depth(root);
    }
};