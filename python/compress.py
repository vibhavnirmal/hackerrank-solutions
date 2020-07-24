# https://www.hackerrank.com/challenges/compress-the-string/problem

p = list((input()))

count = 0
h = len(p)
prevTmp = None
s = []
prevCount=1
theLen = len(p)
for i, temp in enumerate(p):
    count = count + 1
    if str(prevTmp):
        if int(temp) == prevTmp:
            prevCount = count
            if theLen == i+1:
                l = [prevCount, prevTmp]
                s.append(l)
            continue
        else:
            if prevTmp is not None:
                l = [prevCount, prevTmp]
                s.append(l)
            prevTmp = int(temp)
            count = 1
            prevCount = 1
            if theLen == i+1:
                l = [prevCount, prevTmp]
                s.append(l)
    else:
        prevTmp = int(temp)
        if theLen == i+1:
            l = [prevCount, prevTmp]
            s.append(l)
        continue


print(*[tuple(i) for i in s])
