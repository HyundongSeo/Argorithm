import sys

a,b = map(int,sys.stdin.readline().split())
N = int(input())

arr=[]
for i in range(N):
    arr.append(int(sys.stdin.readline())) # 즐찾된 주파수

min_gap = 1001
idx = 0
for i in arr:
    temp = abs(i-b) #즐찾주파수 - 목표주파수
    if min_gap > temp:
        min_gap = temp
        idx = i # 최소를 찾으면 min_gap이 바뀌고 즐찾 주파수 값을 idx

print(min(abs(a-b), (abs(idx-b)+1)))