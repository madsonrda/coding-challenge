from heap import heap

def main():
    A = map(int,raw_input().split())
    h = heap(A)
    h.heapsort()
    h.printheap()


if __name__ == '__main__':
    main()
