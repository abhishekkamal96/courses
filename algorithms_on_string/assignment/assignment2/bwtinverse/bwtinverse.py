# python3
import sys


def first_to_last(bwt):
    counts = {'$': 0, "A": 0, 'C': 0, 'G': 0, 'T': 0}
    for char in bwt:
        counts[char] += 1
    temp_count = {'$': 0}
    sum_so_far = counts['$']
    for char in ['A', 'C', 'G', 'T']:
        temp_count[char] = sum_so_far
        sum_so_far += counts[char]
    arr = [0] * len(bwt)
    for i in range(len(bwt) - 1, -1, -1):
        arr[i] = counts[bwt[i]] + temp_count[bwt[i]] - 1
        counts[bwt[i]] -= 1
    return arr


# def InverseBWT(bwt):
#     # write your code here
#
#     f2l = first_to_last(bwt)
#     # print('f2l ', f2l)
#     cur = 0
#     out = '$'
#     for _ in range(1, len(bwt)):
#         out = bwt[cur] + out
#         cur = f2l[cur]
#         # s += bwt[cur] # s = s + bwt[cur]
#         # cur = f2l[cur]
#     return out


def inverse_bwt(bwt):
    last = [(val, idx) for (idx, val) in enumerate(bwt)]
    first = sorted(last)
    first_to_last = {f: l for f, l in zip(first, last)}

    next = first[0]
    result = ''
    for i in range(len(bwt)):
        result += next[0]
        next = first_to_last[next]

    return result[::-1]

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(inverse_bwt(bwt))