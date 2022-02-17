
A = [3, 5, 2, 3, 1, 0, 13]

def merge(A, p, q, r):
	print(f'p: {p}, q: {q}, r: {r}')
	n1 = q - p + 1
	print(f'N1: {n1}')
	n2 = r - q
	print(f'N2: {n2}')
	L = []
	R = []
	for i in range(0, n1):
		L.append(A[p + i - 1])
	for j in range(0, n2):
		R.append(A[q + j])
	L.append(float("inf"))
	R.append(float("inf"))
	print(f'L: {L}')
	print(f'R: {R}')
	i = 0
	j = 0
	for k in range(p, r):
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
		print(f'q: {q}')
		mergeSort(A, p, q)
		mergeSort(A, q + 1, r)
		merge(A, p, q, r)

mergeSort(A, 0, len(A))
print(A)