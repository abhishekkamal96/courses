#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.__stack[-1]
        # return max(self.__stack)

    def size(self):
        return len(self.__stack)

    def get_last(self):
        return self.__stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            if stack.size() > 0:
                last = stack.get_last()
                element = max(last, int(query[1]))
                stack.Push(element)
            else:
                stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
