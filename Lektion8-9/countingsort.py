import time
import random
import math

A = []
B = []
size = 75000
k_value = size * 50

def fillArray():
	A.clear()
	B.clear()
	for i in range(0, size):
		number = random.randint(0, k_value)
		A.append(number)
		B.append(0)

def countingSort(A, B, k):
	C = []
	for i in range(0, k + 1):
		C.append(0)
	for j in range(0, len(A)):
		C[A[j]] = C[A[j]] + 1
	for i in range(0, k):
		C[i + 1] = C[i + 1] + C[i]
	for j in range(len(A) - 1, 0, -1):
		B[C[A[j]] - 1] = A[j]
		C[A[j]] = C[A[j]] - 1

fillArray()
startTime1 = time.time()
countingSort(A, B, k_value)
endTime1 = time.time()
time1 = endTime1 - startTime1

fillArray()
startTime2 = time.time()
countingSort(A, B, k_value)
endTime2 = time.time()
time2 = endTime2 - startTime2

fillArray()
startTime3 = time.time()
countingSort(A, B, k_value)
endTime3 = time.time()
time3 = endTime3 - startTime3

average = ((time1 + time2 + time3) / 3) * 1000
divided = average / size
print(f'Time1: {time1}, time2: {time2}, time3: {time3} seconds\nAverage: {average} miliseconds\naverage / n: {divided}')