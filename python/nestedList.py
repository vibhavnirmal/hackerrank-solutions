#https://www.hackerrank.com/challenges/nested-list/problem


def lowestMarks(theList):
    names = []
    theList.sort(key=lambda x:x[1])
    # print(theList)
    minScore = min(theList, key=lambda x: x[1])
    # print(minScore[1])
    while min(theList, key=lambda x: x[1])[1] == minScore[1]:
        theList.remove(min(theList, key=lambda x: x[1]))
        # print("yolo")
    secondMinScore = min(theList, key=lambda x: x[1])
    # print(secondMinScore)
    while min(theList, key=lambda x: x[1])[1] == secondMinScore[1]:
        # theList.remove(min(theList, key=lambda x: x[1]))
        names.append(min(theList, key=lambda x: x[1])[0])
        # print(names)
        theList.remove(min(theList, key=lambda x: x[1]))
        if theList:
            pass
        else:
            break
        # print(theList, names)
    names.sort()
    return names

if __name__ == '__main__':
    myList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        myList.append([name, score])
    # print(myList)
    g = lowestMarks(myList)
    for i in g:
        print(i)

# 4
# Rachel
# -50
# Mawer
# -50
# Sheen
# -50
# Shaheen
# 51

# 4
# Prashant
# 32
# Pallavi
# 36
# Dheeraj
# 39
# Shivam
# 40
