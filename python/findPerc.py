#https://www.hackerrank.com/challenges/finding-the-percentage/problem

def findPercentage(thedict, query):
    if thedict[query]:
        print("%.2f"%float(sum(thedict[query])/int(len(thedict[query]))))


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    findPercentage(student_marks, query_name)