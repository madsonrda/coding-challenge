def reverse(array):
    temp = 0
    for i in range(len(array)/2):
        temp = array[i]
        array[i] = array[-i-1]
        array[-i-1] = temp

def main():
    '''
    the input could is a string:
    bahia
    '''
    array = list(raw_input())
    reverse(array)
    print("".join(array))

if __name__ == '__main__':
    main()
