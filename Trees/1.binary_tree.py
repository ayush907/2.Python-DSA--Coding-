# creating a tree node
class Node:

    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class tree:
     
    idx = -1

    # build tree preorder
    def build_tree_preorder(self, nodes_arr = []):
         
        self.idx = self.idx + 1

        if nodes_arr[self.idx] == -1:
             return None
         
        newnode = Node(nodes_arr[self.idx])
        newnode.left = self.build_tree_preorder(nodes_arr)
        newnode.right = self.build_tree_preorder(nodes_arr)

        return newnode
     

    # preorder traversal in a binary tree
    def preorder_traversal(self, root):
        if root is not None:
            print(root.data, end = " ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    
    # postorder traversal in a binary tree
    def postorder_traversal(self, root):
        if root == None:
            return
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        print(root.data, end = " ")


    # inorder traversal in a binary tree
    def inorder_traversal(self, root):
        if root != None:
            self.inorder_traversal(root.left)
            print(root.data, end = " ")
            self.inorder_traversal(root.right)
    

    # level order traversal in a tree (BFS in a tree)
    def level_order_traversal(self, root):
        if root is None:
            return
        
        q = list()     # using list as a queue
        q.append(root)
        q.append(None)

        while q != None:
            currnode = q.pop(0)   # extracting the first element(Node)
            if currnode == None:
                print()
                if len(q) == 0:
                    break
                else:
                    q.append(None)
            
            else:
                print(currnode.data, end = " ")
                if currnode.left != None:
                    q.append(currnode.left)
                if currnode.right != None:
                    q.append(currnode.right)

    
    # height of a binary tree
    def height_bt(self, root):
        if root == None:
            return 0
        
        left_height = self.height_bt(root.left)
        right_height = self.height_bt(root.right)

        return max(left_height, right_height) + 1
    

    # count of nodes in a binary tree
    def count_nodes(self, root):
        if root == None:
            return 0
        
        left_count = self.count_nodes(root.left)
        right_count = self.count_nodes(root.right)

        return left_count + right_count + 1
    
    
    # calculating the sum nodes
    def sum_of_nodes(self, root):
        if root == None:
            return 0
        
        left_sum = self.sum_of_nodes(root.left)
        right_sum = self.sum_of_nodes(root.right)

        return left_sum + right_sum + root.data
    

    # calculating the diameter of the tree
    def diameter(self, root):
        if root == None:
            return 0
        
        left_diam = self.diameter(root.left)
        right_diam = self.diameter(root.right)
        left_height = self.height_bt(root.left)
        right_height = self.height_bt(root.right)

        self_diam = left_height + right_height + 1

        return max(max(left_diam, right_diam), self_diam)
    


t = tree()
nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
root = t.build_tree_preorder(nodes)
t.inorder_traversal(root)
print()
t.preorder_traversal(root)
print()
t.postorder_traversal(root)
print()
t.level_order_traversal(root)
print()
print(t.height_bt(root))
print(t.count_nodes(root))
print(f"the diameter of tree is {t.diameter(root)}")