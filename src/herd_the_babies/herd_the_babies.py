
def herd_the_babies(stringWords):
    finalStr = ''
    sortString = sorted(stringWords, key=str.casefold)
    newStr = ''.join(sortString)

    for index, string in enumerate(newStr):
        if index > 0:
            if (newStr[index -1] > newStr[index]) == False:
                print([index -1])
                finalStr += newStr[index-1]
      
    print(finalStr)