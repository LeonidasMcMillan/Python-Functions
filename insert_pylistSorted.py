def insert(inputList, n):
	if len(inputList) == 0:
		inputList.append(n)
		return inputList
	if n > inputList[len(inputList)-1]:
		inputList.append(n)
		return inputList
	for i in range(len(inputList)):
    	if inputList[i] > n:
        	index = i
        	break
	result = inputList[: i] + [n] + inputList[i :]
	return result
