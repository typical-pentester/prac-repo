def exampleFunction():
    letters = list(range(65, 75))
    for index, num in enumerate(letters):
        print(index, num)


def sortList(givenList):
    print(sorted(givenList, reverse=False))
    givenList.sort(reverse=True)
    print(givenList)


exampleFunction()
sendList = list(range(1, 20))
sortList(sendList)
print("Hello ")
print("world")
