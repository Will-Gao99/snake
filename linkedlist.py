

class Node:

    def __init__(self, v, n = None):
        self.val = v
        self.next = n

    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n

    def get_val(self):
        return self.val

    def set_val(self, val):
        self.val = val

    """
    Returns True if this node has a succesor and False otherwise
    """
    def has_next(self):
        return not self.next == None

    def to_string(self):
        pass

class LinkedList:

    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def get_last(self):
        this_node = self.root
        while this_node is not None:
            if this_node.get_next() == None:
                return this_node
            else:
                this_node = this_node.get_next()

    def prepend(self, v):
        new_node = Node(v, self.root)
        self.root = new_node
        self.size += 1

    def append(self, v):
        self.get_last().set_next(Node(v))
        self.size += 1

    def remove(self, v):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.get_val() == v:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True # Node removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False # Node not found

    def find(self, v):
        this_node = self.root
        while this_node is not None:
            if this_node.get_val() == v:
                return v
            elif this_node.get_next() == None:
                return False
            else:
                this_node = this_node.get_next()




#
