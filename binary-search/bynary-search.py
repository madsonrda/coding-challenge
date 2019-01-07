import math
def main():
    '''
    input:
    first line is the integer value to be found in the sorted array
    second line is a sorted integer list with the numbers separated by blank space.
    ex:
    2
    1 2 4 7 9 11
    '''
    value = int(raw_input())
    array = map(int,raw_input().split())
    bs = BinarySearch(array,value)
    print(bs)

def BinarySearch(array,value):
    '''
    array: sorted int list
    value: value to be found in the list
    return: if the value was found retunr the index of the list, else return -1
    '''
    l = 0
    r = len(array) -1
    pivot = int(math.floor((l+r)/2))

    while l <= r:
        if array[pivot] < value:
            l = pivot + 1
            pivot = int(math.floor((l+r)/2))
        elif array[pivot] > value:
            r = pivot -1
            pivot = int(math.floor((l+r)/2))
        else:
            return pivot

    return -1

if __name__ == '__main__':
    main()
