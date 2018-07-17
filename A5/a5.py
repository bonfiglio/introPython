class Node(object):
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.val = val


class BinarySearchTree(object):
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        # if root is None:
        #    return node
        temp = self.root
        temp_child = temp
        while temp is not None:
            if temp.val < val:
                if temp.r_child is None:
                    temp.r_child = Node(val)
                    break
                else:
                    temp = temp.r_child
            else:
                if temp.l_child is None:
                    temp.l_child = Node(val)
                    break
                else:
                    temp = temp.l_child

        return self

    def in_order_place(self, root):
        if not root:
            return 'end'
        else:
            self.in_order_place(root.l_child)
            print(root.val, end='-')
            self.in_order_place(root.r_child)

    def in_order(self):
        ordinati = []

        def in_order_node(root):
            if root.l_child:
                in_order_node(root.l_child)
            ordinati.append(root.val)
            if root.r_child:
                in_order_node(root.r_child)

        in_order_node(self.root)
        return ordinati

    def pre_order(self):
        ordinati = []

        def pre_order_node(root):
            ordinati.append(root.val)
            if root.l_child:
                pre_order_node(root.l_child)
            if root.r_child:
                pre_order_node(root.r_child)

        pre_order_node(self.root)
        return ordinati

    def pre_order_place(self, root):
        if not root:
            return ''
        else:
            print(root.val, end='-')
            self.pre_order_place(root.l_child)
            self.pre_order_place(root.r_child)

    def post_order(self):
        ordinati = []

        def post_order_node(root):
            if root.l_child:
                post_order_node(root.l_child)
            if root.r_child:
                post_order_node(root.r_child)
            ordinati.append(root.val)

        post_order_node(self.root)
        return ordinati

    def post_order_place(self, root):
        if not root:
            return ''
        else:
            self.post_order_place(root.l_child)
            self.post_order_place(root.r_child)
            print(root.val, end='-')

    def delete_node(self, val):
        temp = self.root
        temp_padre = temp
        child = 'r'
        while temp is not None:
            if temp.val < val:
                temp_padre = temp
                child = 'r'
                temp = temp.r_child
            elif temp.val > val:
                temp_padre = temp
                child = 'l'
                temp = temp.l_child
            else:

                # case 1. When the node to be deleted is a leaf node then simply delete the node and pass nullptr to its parent node.
                if temp.r_child is None and temp.l_child is None:
                    # temp = None
                    if child == 'r':
                        temp_padre.r_child = None
                    else:
                        temp_padre.l_child = None
                    break
                # case 2. When a node to be deleted is having only one child then copy the child value to the node value and delete the child (Converted to case 1)
                if temp.r_child is None and temp.l_child is not None:
                    # temp = temp.l_child
                    if child == 'r':
                        temp_padre.r_child = temp.l_child
                    else:
                        temp_padre.l_child = temp.l_child
                    break

                if temp.r_child is not None and temp.l_child is None:
                    # temp = temp.r_child
                    if child == 'r':
                        temp_padre.r_child = temp.r_child
                    else:
                        temp_padre.l_child = temp.r_child
                    break
                # case3. When a node to be delete is having two childs then the minimum from its right sub tree can be copied to the node and then the minimum value can be deleted from the node's right subtree (Converted to Case 2)
                root = temp
                temp_padre = temp
                temp = temp.l_child
                child = 'l'
                while temp.r_child is not None:
                    temp_padre = temp
                    temp = temp.r_child
                    child = 'r'
                root.val = temp.val
                if child == 'r':
                    temp_padre.r_child = temp.l_child
                else:
                    temp_padre.l_child = temp.r_child
                break

        return


# r = Node(3)
bstnode = BinarySearchTree(3)
nodeList = [1, 8, 7, 6, 5, 12, 4, 5, 14, 6, 15, 7, 16, 8]
for nd in nodeList:
    bstnode.insert(nd)

print("------In order -LVR-----")
print(bstnode.in_order())
print("------Pre order -VLR-----")
bstnode.delete_node(6)
print(bstnode.in_order())
bstnode.delete_node(5)
print(bstnode.in_order())
bstnode.delete_node(8)
print(bstnode.in_order())
# print(node.pre_order_place(r))
# print("------Post order -LRV------")
# print(node.post_order_place(r))
