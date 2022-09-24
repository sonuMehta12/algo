from math import ceil, floor



heap2 = [0, 10 , 20 , 30 , 25, 5, 40, 35 ]

def insert2 ( heap, n):
    temp, i = None, n
    temp = heap[n]
    while(i > 1 and temp > heap[ floor(i/2)]): ## min max > <
        heap[i] = heap[floor(i/2)]
        i = floor(i/2)
    heap[i] = temp

def heapify(arr, n):
    i = n
    while(i >=1):
        j = i *2
        if(j  <= n ):
            k  = 0 if j +1 > n else arr[j+1] #ternary
            if(arr[j] < k ):
                j = j+1
            if(arr[i] < arr[j]):
                arr[i], arr[j] = arr[j] , arr[i]
        i = i-1

   
heapify(heap2, len(heap2)-1) 

#83 75 07 38 20  subhash bhai egs


def create_heap(array):
    i = 2
    for i in range(8):
        heapify(array, i)
    

create_heap(heap2)

def delele_heap(heap, n):
    temp = heap[1]
    heap[1] = heap[n]
    i = 1
    j = i * 2
    while ( j < n-1 ):
        if(heap[j + 1] > heap[j]):
            j = j+1
        if(heap[i] < heap[j]):
            heap[i] , heap[j] = heap[j] ,heap[i]
            i = j
            j  = 2 * j
        else:
            break
    heap[n] = temp


def heap_sort(heap, n):
    create_heap(heap2)
    while(n >= 1):
        delele_heap(heap, n)
        n = n-1
print(heap2)

heap_sort(heap2, len(heap2)-1)
print(heap2)


    



