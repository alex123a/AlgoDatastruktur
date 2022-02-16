import time
startTime = 0
endTime = 0

A = []
size = 6500
for i in range(size, 0, -1):
    A.append(i)

# for i in range(0, size):
#     A.append(i)

def insertionSort():
    startTime = time.time()
    for j in range(1, len(A)):
        
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    endTime = time.time()
    print(f'It took {endTime - startTime} s to sort the array with length {len(A)}')

insertionSort()


