# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        stack = []
        current = 0
        while True:
            if current != -1:
                stack.append(current)
                current = self.left[current]
            elif stack:
                current = stack.pop()
                self.result.append(self.key[current])
                current = self.right[current]
            else:
                break
        return self.result

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        stack = []
        current = 0
        while True:
            if current != -1:
                self.result.append(self.key[current])
                if self.right[current] != -1:
                    stack.append(self.right[current])
                current = self.left[current]
            elif stack:
                current = stack.pop()
                self.result.append(self.key[current])
                if self.right[current] != -1:
                    stack.append(self.right[current])
                current = self.left[current]
            else:
                break

        return self.result

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        stack = []
        current = 0
        while True:
            if current != -1:
                if self.right[current] != -1:
                    stack.append(self.right[current])
                stack.append(current)
                current = self.left[current]
            elif stack:
                current = stack.pop()
                if stack and stack[-1] == self.right[current]:
                    stack.pop()
                    stack.append(current)
                    current = self.right[current]
                else:
                    self.result.append(self.key[current])
                    current = -1
            else:
                break

        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    # print("key ", tree.key)
    # print("left ", tree.left)
    # print("right", tree.right)
    # root = tree.key[0]
    # ino = tree.inOrder(root)
    # print(" ".join(str(x) for x in ino))

    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
