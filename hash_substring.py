# Emīlija Ostaševska 221RDB231 4.grupa

def read_input():

    fi = input()

    if "I" in fi or "i" in fi:
        n = input().rstrip()
        data = input().rstrip()
        
    elif "F" in fi or "f" in fi:
        with open(f"tests/06", "r") as file:
            n = file.readline().rstrip()
            data = file.readline().rstrip()

    return n, data
    

def print_occurrences(output): 
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):

    result = []
    hash_pattern = hash(pattern)

    t_len = len(text)
    p_len = len(pattern)

    for i in range(t_len - p_len + 1):
        hash_text = hash(text[i:i + p_len])
        if hash_text == hash_pattern and pattern == text[i:i + p_len]:
            result.append(i)

    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
    