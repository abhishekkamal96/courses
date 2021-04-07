# python3
import sys


def compute_prefix_function(p):
  n = len(p)
  s = [-1 for i in range(n)]
  s[0] = 0
  border = 0
  for i in range(1, n):
    while border > 0 and p[border] != p[i]:
      border = s[border - 1]
    if p[border] == p[i]:
      border += 1
    else:
      border = 0
    s[i] = border
  return s


def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  result = []
  # Implement this function yourself
  p = pattern + '$' + text
  s = compute_prefix_function(p)
  for i in range(len(pattern), len(s)):
    if s[i] == len(pattern):
      result.append(i - 2*len(pattern))

  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

