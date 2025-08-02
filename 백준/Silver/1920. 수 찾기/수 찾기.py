import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()   # 이진 탐색은 정렬된 배열 필요

def Binary(b):
    start = 0
    end = N -1
    find = False

    while start <= end:
        mid = int((start + end)/2)

        if A[mid] > b:
            end = mid - 1
        elif A[mid] < b:
            start = mid + 1
        else:
            find = True
            break
    
    if find == True:
        print(1)
    else:
        print(0)

for b in B:
    Binary(b)