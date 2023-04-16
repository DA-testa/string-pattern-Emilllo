# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    fi = input()

    if "I" in fi or "i" in fi:
        n = input().rstrip()
        data = input().rstrip()
        

    elif "F" in fi or "f" in fi:
        #test_num = input("Choose test number (only 06 lol): ")
        with open(f"tests/06", "r") as file:
            n = file.readline().rstrip()
            data = file.readline().rstrip()
            # print(f"N: ",n ,"data: ", data)

    return n, data
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm

    result = []
    hash_pattern = hash(pattern)

    t_len = len(text)
    p_len = len(pattern)

    for i in range(t_len - p_len + 1):
        hash_text = hash(text[i:i + p_len])
        if hash_text == hash_pattern and pattern == text[i:i + p_len]:
            result.append(i)
    return result

    # and return an iterable variable
    # return [0]

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))