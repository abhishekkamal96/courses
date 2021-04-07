# python3
import sys

def BWT(text):
    out = ""
    bwt_mat = []
    n = len(text)
    bwt_mat.append(text)
    for i in range(1, n):
        text = text[-1] + text[:-1]
        bwt_mat.append(text)

    bwt_mat.sort()
    for element in bwt_mat:
        out = out + element[-1]
    return out

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    # text = "AA$"
    print(BWT(text))