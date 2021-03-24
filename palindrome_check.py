def isPalindrome(string):
    stringList = list(string)
    if len(stringList) == 0 or len(stringList) == 1:
        return True
    while len(stringList) > 1:
        if stringList[0] == stringList[len(stringList)-1]:
            stringList.pop(0)
            stringList.pop(len(stringList)-1)
            if len(stringList) == 1 or len(stringList) == 0:
                return True
        else:
            return False