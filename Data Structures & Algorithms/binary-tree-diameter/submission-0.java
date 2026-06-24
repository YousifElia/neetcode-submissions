/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    int diameter;
    public int diameterOfBinaryTree(TreeNode root) {
        diameter = 0;
        dfs(root);
        return diameter;
    }
    private int dfs(TreeNode root) {
        if(root == null) {
            return 0;
        }
        int LeftPath = dfs(root.left);
        int RightPath = dfs(root.right);
        diameter = Math.max(diameter, LeftPath + RightPath);
        return 1 + Math.max(LeftPath, RightPath);
    }
}
