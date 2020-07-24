#https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    p = []
    for i in range(N):
        p.append(input().split())
    
    finalList=[]
    for listValue in p:
        if listValue[0] == "insert":
            finalList.insert(int(listValue[1]),int(listValue[2]))
        if listValue[0] == "print":
            print(finalList)
        if listValue[0] == "remove":
            finalList.remove(int(listValue[1]))
        if listValue[0] == "append":
            finalList.append(int(listValue[1]))
        if listValue[0] == "sort":
            finalList.sort()
        if listValue[0] == "pop":
            finalList.pop()
        if listValue[0] == "reverse":
            finalList.reverse()