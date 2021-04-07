# python3
import sys


def sort_charecters(s):
  order = [0] * len(s)
  count = {'$': 0, "A": 0, 'C': 0, 'G': 0, 'T': 0}
  for char in s:
    count[char] += 1
  ele = ['$', 'A', 'C', 'G', 'T']
  for i in range(1, 5):
    count[ele[i]] += count[ele[i - 1]]
  for j in range(len(s) - 1, -1, -1):
    c = s[j]
    count[c] -= 1
    order[count[c]] = j
  return order


def compute_char_classes(s, order):
  char_class = [0] * len(s)
  for i in range(1, len(s)):
    if s[order[i]] == s[order[i - 1]]:
      char_class[order[i]] = char_class[order[i - 1]]
    else:
      char_class[order[i]] = char_class[order[i - 1]] + 1
  return char_class


def sort_doubled(s, L, old_order, old_class):
  count = [0] * len(s)
  new_order = [0] * len(s)
  for i in range(len(s)):
    count[old_class[i]] += 1
  for i in range(1, len(s)):
    count[i] += count[i - 1]
  for j in range(len(s) - 1, -1, -1):
    start = (old_order[j] - L + len(s)) % len(s)
    cl = old_class[start]
    count[cl] -= 1
    new_order[count[cl]] = start
  return new_order


def update_classes(new_order, old_class, L):
  n = len(new_order)
  new_class = [0] * n
  for i in range(1, n):
    cur = new_order[i]
    mid = (cur + L) % n
    prev = new_order[i - 1]
    mid_prev = (prev + L) % n
    if old_class[cur] == old_class[prev] and old_class[mid] == old_class[mid_prev]:
      new_class[cur] = new_class[prev]
    else:
      new_class[cur] = new_class[prev] + 1
  return new_class


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  # result = []
  # Implement this function yourself
  order = sort_charecters(text)
  _class = compute_char_classes(text, order)
  L = 1
  while L < len(text):
    order = sort_doubled(text, L, order, _class)
    _class = update_classes(order, _class, L)
    L = 2 * L
  return order


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
