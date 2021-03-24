def selectionSort(array):
    output = [array[0]]
    array.pop(0)
    return selSortHelp(array, output)

def insert(inputList, n):
    if n > inputList[len(inputList)-1]:
        inputList.append(n)
        return inputList
    for i in range(len(inputList)):
        if inputList[i] > n:
            index = i
            break
    result = inputList[: i] + [n] + inputList[i :]
    return result

def selSortHelp(inputA, outputA):
    if len(inputA) == 0:
        return outputA
    if len(inputA) == 1:
        outputA = insert(outputA,inputA[0])
        return outputA
    else:
        outputA = insert(outputA,inputA[0])
        inputA.pop(0)
        return selSortHelp(inputA,outputA)
