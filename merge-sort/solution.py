 def Merge(A,L,R):
    L += [float('inf')]
    R += [float('inf')]
    i = 0
    j = 0
    for k in range(len(A)):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j+=1


def MergeSort(A):
    if len(A) > 1:
        m = len(A)//2
        L = A[:m]
        R = A[m:]
        MergeSort(L)
        MergeSort(R)
        Merge(A,L,R)


def main():
    '''
    input: list of numbers separated by space, ex:
    1 2 3 4 5
    '''
    A = map(int,raw_input().split())
    import numpy as np
    MergeSort(A)
    print(A)

if __name__ == '__main__':
    main()
