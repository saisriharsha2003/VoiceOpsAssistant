def findLongWord(input1):
    if len(input1)<=10:
        return input1
    else:
        return input1[0]+str(len(input1)-2)+input1[-1]
print(findLongWord("internationalization"))