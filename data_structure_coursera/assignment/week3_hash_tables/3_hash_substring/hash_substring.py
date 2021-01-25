# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # print("text ", text, "pattern ", pattern)
    result = []
    hash_pattern = hash(pattern)
    len_pattern = len(pattern)
    for i in range(len(text) - len(pattern) + 1 ):
        temp = text[i:i+len_pattern]
        if hash(temp) != hash_pattern:
            continue
        else:
            if temp == pattern:
                result.append(i)

    return result



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

