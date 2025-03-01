# creating a tree node
class Node:

    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class info:       # tree diametr calculate karne mai use hogi ye

    def __init__(self, diam, ht):
        self.diam = diam
        self.ht = ht


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
    def diameter_first(self, root):
        if root == None:
            return 0
        
        left_diam = self.diameter_first(root.left)
        right_diam = self.diameter_first(root.right)
        left_height = self.height_bt(root.left)
        right_height = self.height_bt(root.right)

        self_diam = left_height + right_height + 1

        return max(max(left_diam, right_diam), self_diam)
    

    # calculating diamaeter of the tree second approach
    def diameter_second(self, root):
        if root == None:
            return info(0, 0)  # ek info object return kar rahe hai jisme diameter orr height hai
        
        left_info = self.diameter_second(root.left)
        right_info = self.diameter_second(root.right)

        diam = max(max(left_info.diam, right_info.diam), left_info.ht + right_info.ht + 1)
        curr_ht = max(left_info.ht, right_info.ht) + 1

        return info(diam, curr_ht)
    

    '''given roots of two binary trees root and subroot return true if there is a subtree of root with
       the same structure and node values of subroot and false otherwise.
       >> we will create two functions here (is_identical and is_subtree)   
       is_identical is used as the helper function. 
    ''' 
    def is_identical(self, node, subroot):
        if node == None and subroot == None:
            return True  
        elif node == None or subroot == None or node.data != subroot.data:
            return False
        
        if not self.is_identical(node.left, subroot.left):
            return False
        if not self.is_identical(node.right, subroot.right):
            return False
        
        return True
    
    def is_subtree(self, root, subroot):
        if root == None:
            return False
        
        if root.data == subroot.data:
            if self.is_identical(root, subroot):
                return True
            
        left_ans = self.is_subtree(root.left, subroot)
        right_ans = self.is_subtree(root.right, subroot)

        return left_ans or right_ans
    


# t = tree()
# nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
# root = t.build_tree_preorder(nodes)
# t.inorder_traversal(root)
# print()
# t.preorder_traversal(root)
# print()
# t.postorder_traversal(root)
# print()
# t.level_order_traversal(root)
# print()
# print(t.height_bt(root))
# print(t.count_nodes(root))
# print(f"the diameter by first approach of tree is {t.diameter_first(root)}")
# print(f"the diameter by second approach is {t.diameter_second(root).diam} and height {t.diameter_second(root).ht}")

t2 = tree()

# creating a tree
root = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

root.left = two
root.right = three
two.left = four
two.right = five
three.right = six

# creating a subtree
subroot = Node(2)
sub_two = Node(4)
sub_three = Node(5)

subroot.left = sub_two
subroot.right = sub_three

t2.level_order_traversal(root)
print()
t2.level_order_traversal(subroot)
print()
print(t2.is_subtree(root, subroot))