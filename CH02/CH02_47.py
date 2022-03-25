numList = [10,20,30,40,50]
print("주어진 수:", numList)
myNumber = int(input("Enter number: "))
for anyNumber in numList:
    if anyNumber > myNumber:
        print(anyNumber, "<", myNumber)
    else:
        print(anyNumber, "<=", myNumber)
