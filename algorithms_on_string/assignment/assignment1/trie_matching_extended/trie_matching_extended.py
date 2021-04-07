# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4
		self.patternEnd = False

def build_trie(patterns):
    tree = dict()
    # write your code here
    # tree = {0:{'A':1,'T':2},1:{'C':3}}]
    tree[0] = {}
    node_count = 1
    for pattern in patterns:
        cnode = 0
        for char in pattern:
            if char in tree.get(cnode, {}):
                cnode = tree[cnode].get(char)
            else:
                if tree.get(cnode):
                    tree[cnode][char] = node_count
                else:
                    node = {char: node_count}
                    tree[cnode] = node
                cnode = node_count
                node_count += 1
    return tree


def solve (text, n, patterns):
    trie = build_trie(patterns)
    result = []
    for i in range(len(text)):
        cnode = 0
        j = i
        while True and j < len(text):
            char = text[j]
            if "$" in trie.get(cnode, {}):
                result.append(i)
                break
            elif char in trie.get(cnode, {}):
                cnode = trie.get(cnode).get(char)
                j += 1
                if "$" in trie.get(cnode, {}):
                    result.append(i)
                    break
            else:
                break

    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    patterns = []
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]
    for i in range(n):
        patterns[i] = patterns[i] + "$"
    # print('text ', text)
    # print('patterns', patterns)
    # print('n', n)
    # text, n, patterns = "AAA", 1, ["AA$"]
    # text, n, patterns = "ACATA", 3, ["AT$", "A$", "AG$"]
    # text, n, patterns = "AA", 1, ["T$"]
    # text, n, patterns = "AATCGGGTTCAATCGGGGT", 1, ["ATCG$",  "GGGT$"]
    # print('trie ', tre)
    ans = solve(text, n, patterns)
    sys.stdout.write(' '.join(map(str, ans)) + '\n')
