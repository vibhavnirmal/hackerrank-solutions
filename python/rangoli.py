#https://www.hackerrank.com/challenges/alphabet-rangoli

def print_rangoli(size):
    for i in range(1, size):
        for j in range(1, size):
            print("-"*i)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)