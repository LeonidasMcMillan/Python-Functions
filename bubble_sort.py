def bubbleSort(array):
    for x in range( 0, len(array) - 1 ):
		change = False
		for y in range( 0, len(array) - 1 ):
			if y == len(array) - 1:
				continue
			if array[y] > array[y + 1]:
				array[y], array[y + 1] = array[y + 1], array[y]
				change = True
			continue
		if change == False:
			break
    return array