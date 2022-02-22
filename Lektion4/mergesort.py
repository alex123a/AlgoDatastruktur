import time
import random
import math

A = []
size = 125000

def fillArray():
	A.clear()
	for i in range(0, size + 1):
		number = random.randint(1, 300)
		A.append(number)

def merge(A, p, q, r):
	n1 = q - p + 1
	n2 = r - q
	L = []
	R = []
	for i in range(0, n1):
		L.append(A[p + i])
	for j in range(0, n2):
		R.append(A[q + j + 1])
	L.append(float("inf"))
	R.append(float("inf"))
	i = 0
	j = 0
	# Count is for task 4
	count = 0
	for k in range(p, r + 1):
		# Task 4 start
		if i < j and L[i] > R[j]:
			# print(count)
			count += 1
		# Task 4 end
		if L[i] <= R[j]:
			A[k] = L[i]
			i = i + 1
		else:
			A[k] = R[j]
			j = j + 1
	return A

def mergeSort(A, p, r):
	if p < r:
		q = (p + r) // 2
		mergeSort(A, p, q)
		mergeSort(A, q + 1, r)
		merge(A, p, q, r)

fillArray()
startTime1 = time.time()
mergeSort(A, 0, len(A) - 1)
endTime1 = time.time()
time1 = endTime1 - startTime1

fillArray()
startTime2 = time.time()
mergeSort(A, 0, len(A) - 1)
endTime2 = time.time()
time2 = endTime2 - startTime2

fillArray()
startTime3 = time.time()
mergeSort(A, 0, len(A) - 1)
endTime3 = time.time()
time3 = endTime3 - startTime3

average = ((time1 + time2 + time3) / 3) * 1000
divided = average / (size * math.log(size, 2))
print(f'Time1: {time1}, time2: {time2}, time3: {time3} seconds\nAverage: {average} miliseconds\naverage / n * log n: {divided}')