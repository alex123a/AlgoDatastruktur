import time
import random
import math

A = []
size = 12000

def fillArray():
	A.clear()
	for i in range(0, size + 1):
		number = random.randint(1, 300)
		A.append(number)

def partition(A, p, r):
	x = A[r]
	i = p - 1
	for j in range(p, r):
		if A[j] <= x:
			i = i + 1
			temp = A[i]
			A[i] = A[j]
			A[j] = temp
	temp2 = A[i + 1]
	A[i + 1] = A[r]
	A[r] = temp2
	return i + 1


def quickSort(A, p, r):
	if p < r:
		q = partition(A, p, r)
		quickSort(A, p, q - 1)
		quickSort(A, q + 1, r)

fillArray()
startTime1 = time.time()
quickSort(A, 0, len(A) - 1)
endTime1 = time.time()
time1 = endTime1 - startTime1

fillArray()
startTime2 = time.time()
quickSort(A, 0, len(A) - 1)
endTime2 = time.time()
time2 = endTime2 - startTime2

fillArray()
startTime3 = time.time()
quickSort(A, 0, len(A) - 1)
endTime3 = time.time()
time3 = endTime3 - startTime3

average = ((time1 + time2 + time3) / 3) * 1000
divided = average / (size * math.log(size, 2))
print(f'Time1: {time1}, time2: {time2}, time3: {time3} seconds\nAverage: {average} miliseconds\naverage / n * log n: {divided}')