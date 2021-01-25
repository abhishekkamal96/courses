#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def get_inorder(tree):
  if not tree:
    return []
  ino = []
  stack = []
  current = 0
  while True:
    if current != -1:
      stack.append(current)
      current = tree[current][1]
    elif stack:
      current = stack.pop()
      ino.append(tree[current][0])
      current = tree[current][2]
    else:
      break
  return ino

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  ino = get_inorder(tree)
  for i in range(1, len(ino)):
    if ino[i] < ino[i - 1]:
      return False

  for i in range(len(tree)):
    key = tree[i][0]
    left = tree[i][1]
    if left != -1 and tree[left][0] >= key:
      # print("i ", i, key, left)
      return False
  return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
