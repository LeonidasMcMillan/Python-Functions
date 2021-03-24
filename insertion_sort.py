def insertionSort(array):
    if len(array) == 1:
		return array
    key = 1
    for x in range(key, len(array)+1):
		passkey = key

		if passkey == len(array) :
			return array
		
		while array[passkey] < array[passkey - 1] and (passkey - 1) >= 0:
			
			array[passkey], array[passkey - 1] = array[passkey -1], array[passkey]
			passkey = passkey - 1
			
		key = key + 1
		
		
	
		