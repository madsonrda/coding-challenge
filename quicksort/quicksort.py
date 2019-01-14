def partition(A,l,r):
    p = A[r]
    i = l-1
    for j in range(l,r):
        if A[j] <= p:
            i+=1
            temp=A[j]
            A[j]=A[i]
            A[i]= temp
    A[i+1],A[r] = A[r],A[i+1]
    return i+1


def quicksort(A,l,r):
    if l < r:
        p = partition(A,l,r)
        quicksort(A,l,p-1)
        quicksort(A,p+1,r)



A = map(int,raw_input().split())
quicksort(A,0,len(A)-1)
print(A)
