class Node():
    def __init__(self, p, left, right, color, key):
        self.p = p
        self.left = left
        self.right = right
        self.color = color
        self.key = key


class RedBlackTree():
    # each node with color -- red or black
    # root -- black
    # each leaf node -- black
    # if a node is red -- its children are black
    # for each node, on the path from itself to its any descendent's leaf, there are same num of black node

    # black height: num of black node from itself to its any leaf (do not include itself)
    def __init__(self, root):
        self.root = root
        self.NIL = None
        self.root.p = self.NIL

    def minimum(self, root):
        x = root
        if x and x != self.NIL:
            while x.left and x.left != self.NIL:
                x = x.left
            return x
        else:
            return None

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.p = x
        # else: y.left is NIL -- its p can be any value

        y.p = x.p

        if x.p == self.NIL:
            self.root = y
        elif x == x.p.left: # if x is the left child
            x.p.left = y
        else: # if x is the right child
            x.p.right = y

        y.left = x
        x.p = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.p = y
        # else: x.right is NIL -- its p can be any value

        x.p = y.p

        if y.p == self.NIL:
            self.root = x
        elif y == y.p.left: # if y is the left child
            y.p.left = x
        else: # if y is the right child
            y.p.right = x

        x.right = y
        y.p = x

    def rb_insert_fixup(self, z):
        while z.p.color == 'r':
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == 'r':
                    z.p.color = 'b'
                    y.color = 'b'
                    z.p.p.color = 'r'
                    z = z.p.p

                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)

                    z.p.color = 'b'
                    z.p.p.color = 'r'
                    self.right_rotate(z.p.p)

            else:
                y = z.p.p.left
                if y.color == 'r':
                    z.p.color = 'b'
                    y.color = 'b'
                    z.p.p.color = 'r'
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = 'b'
                    z.p.p.color = 'r'
                    self.left_rotate(z.p.p)
        self.root.color = 'b'

    def rb_insert(self, z):
        y = self.NIL
        x = self.root
        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.p = y
        if y == self.NIL:
            self.root = z
        elif z.key<y.key:
            y.left = z
        else:
            y.right = z

        z.left = self.NIL
        z.right = self.NIL
        z.color = 'r'
        self.rb_insert_fixup(z)


    def rb_transplant(self, u, v):
        # u is the node should be deleted, v is the u's child, connect v to u.p
        if u.p == self.NIL:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def rb_delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.p = y

            self.rb_transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == 'b':
            self.re_delete_fixup(x)

    def re_delete_fixup(self, x):
        while x != self.root and x.color == 'b':
            if x==x.p.left:
                w = x.p.right
                if w.color == 'r':
                    w.color = 'b'
                    x.p.color = 'r'
                    self.left_rotate(x.p)
                    w = x.p.right

                if w.left.color == 'b' and w.right.color == 'b':
                    w.color = 'r'
                    x = x.p

                else:
                    if w.right.color == 'b':
                        w.left.color = 'b'
                        w.color = 'r'
                        self.right_rotate(w)
                        w = x.p.right

                    w.color = x.p.color
                    x.p.color = 'b'
                    w.right.color = 'b'
                    self.left_rotate(x.p)
                    x = self.root
            elif x == x.p.right:
                w = x.p.left
                if w.color == 'r':
                    w.color = 'b'
                    x.p.color = 'r'
                    self.right_rotate(x.p)
                    w = x.p.left
                if w.left.color == 'b' and w.right.color == 'b':
                    w.color = 'r'
                    x = x.p

                else:
                    if w.left.color == 'b':
                        w.right.color = 'b'
                        w.color = 'r'
                        self.left_rotate(w)
                        w = x.p.left

                    w.color = x.p.color
                    x.p.color = 'b'
                    w.left.color = 'b'
                    self.right_rotate(x.p)
                    x = self.root
        x.color = 'b'