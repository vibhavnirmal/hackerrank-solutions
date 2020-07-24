#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?h_r=next-challenge&h_v=zen

def runnerUp(arr):
    j = list(arr)
    maxVal = max(j)
    while max(j) == maxVal:
        j.remove(max(j))
    return max(j)


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(runnerUp(arr))