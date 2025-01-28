# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#.         [A,B] -> [D]
 #      

  
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        \\\
        stack = [6]
        #res = [4,2,5,1,3,6]
       root = 6
     left - mid - right
          1
        /   \\
       2     3
      / \\     /
     4-   5.  6

The recursive relation you've provided, T(n) = 2 * T(n/2) + 1, r.

Let's break down the recursive relation and explain how it relates to the in-order traversal:

T(n): This represents the time complexity of the algorithm for a tree of size 'n'.

T(n/2): This term represents the time complexity for traversing the left and right subtrees, each of size 'n/2'. Since we are performing an in-order traversal, we first traverse the left subtree, so the left subtree traversal time is T(n/2). Then we traverse the right subtree, which also has a size of 'n/2', so the right subtree traversal time is also T(n/2).

1: This constant term represents the time it takes to process the current node itself. In an in-order traversal, you process the current node between traversing the left and right subtrees.

So, combining these terms:

T(n) = 2 * T(n/2) + 1
         

        \\\
        st = []
        res = []
        while root or st:
            while root:
                st.append(root)
                root = root.left
                #print(root.left)
            root = st.pop() #2
            #print(root)
            res.append(root.val) #4
            root = root.right #root = 1.right
            #print(root.right)
            
        
        return res


