# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def height(self, tr, root, dp):
            if root not in tr:
                return dp[root]
            if dp[root] != 1:
                return dp[root]
            max_h = 0
            children = tr.get(root)
            for child in children:
                max_h = max(max_h, 1 + self.height(tr, child, dp))
            dp[root] = max_h
            return dp[root]



        def compute_height(self):
                # Replace this code with a faster implementation
                if self.n == 1:
                    return 1
                temp_dict = {}
                for i in range(self.n):
                    if self.parent[i] in temp_dict:
                        temp_dict[self.parent[i]].append(i)
                    else:
                        temp_dict[self.parent[i]] = [i]

                root = temp_dict.get(-1)[0]
                dp = [1 for i in range(self.n)]
                max_height = self.height(temp_dict, root, dp)

                return max_height

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
