import random

n = 16
array = []

for i in range(n):
    array.append(i)

random.shuffle(array)
print(array)
used_index = []
notSkip = True
start_value = -1
def check_next(index, counter):
    used_index.append(index)
    number = array[index]
    if start_value == number:
        print(f'Amount of steps in current cycle {counter}')
        counter = 0
    else:
        # print(i)
        check_next(number, counter + 1)

for i in range(len(array)):
    start_value = i
    # print(i)
    for j in range(len(used_index)):
        if i == used_index[j]:
            notSkip = False
            break

    if (notSkip):
        check_next(i, 1)
    notSkip = True


