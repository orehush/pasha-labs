class Tree:
    def __init__(self, data, parent=None):
        self.left = None
        self.right = None
        self.parent = parent
        self.data = data

    @property
    def children(self):
        result = []
        self.left and result.append(self.left)
        self.right and result.append(self.right)
        return result

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data, parent=self)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data, parent=self)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find(self, value):
        if value == self.data:
            return self

        if value < self.data:
            if self.left is None:
                print('%d not found' % value)
                return
            return self.left.find(value)

        elif value > self.data:
            if self.right is None:
                print('%d not found' % value)
                return
            return self.right.find(value)

    def leafs(self):
        for child in self.children:
            if not child:
                continue
            if not child.children:
                yield child
            yield from child.leafs()

    def repr(self, level=0):
        ret = "\t" * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.repr(level + 1) if child else ''
        return ret

    def delete_child(self, node):
        if not node.children:
            if node == self.left:
                self.left = None
            if node == self.right:
                self.right = None
        else:
            leaf = next(node.leafs())
            node.data = leaf.data
            leaf.delete()

    def delete(self):
        if not self.parent:
            self.data = None
            return
        self.parent.delete_child(self)


if __name__ == '__main__':
    arr = [4, 5, 4, 78, 43, 56, 21, 67, 33, 56, 87, 5, 44]
    root = Tree(arr[0])
    for el in arr[1:]:
        root.insert(el)

    print(root.repr())
    root.find(67).delete()
    print(root.repr())

    root.find(43).delete()
    print(root.repr())

    print(root.find(33))
    print(root.find(1))
