
def isFirst_And_Last_Same(numberList):
  firstElement = numberList[0]
  lastElement =  numberList[-1]
  if(firstElement == lastElement):
    return True
  else:
    return False

numList = [10, 20, 30, 40, 10]

print("The first and last number of a list is same")
print("result is", isFirst_And_Last_Same(numList))
