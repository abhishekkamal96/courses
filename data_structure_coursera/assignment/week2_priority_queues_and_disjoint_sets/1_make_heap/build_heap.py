# python3

def parent(i):
    return (i-1)//2


def leftchild(i):
    return 2*i + 1


def rightchild(i):
    return 2*i + 2


def shiftdown(i, H, size, swap):
    max_index = i
    left = leftchild(i)
    if left < size and H[left] < H[max_index]:
        max_index = left
    right = rightchild(i)
    if right < size and H[right]< H[max_index]:
        max_index = right
    if i != max_index:
        swap.append((i, max_index))
        H[i], H[max_index] = H[max_index], H[i]
        shiftdown(max_index, H, size, swap)
    return H, swap


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    size = len(data)

    for i in range(size // 2, -1, -1):
        data, swaps = shiftdown(i, data, size, swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
