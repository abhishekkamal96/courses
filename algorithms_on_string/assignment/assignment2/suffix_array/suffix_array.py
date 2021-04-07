# python3
import sys


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  # Implement this function yourself
  suffixes = []
  n = len(text)
  for i in range(1, n+1):
    s = text[n-i:n]
    suffix = {"s": s, 'ind': n-i}
    suffixes.append(suffix)
  result = [0]*(n)
  suffixes = sorted(suffixes, key = lambda i:i['s'])
  for i in range(n):
    result[i] = suffixes[i]['ind']
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
