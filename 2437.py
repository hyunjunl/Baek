
import sys
input = sys.stdin.readline

N=int(input())
a= list(map(int, input().split()))
a=sorted(a)
Num=1
for i in range(N):
    if Num<a[i]:
        break
    Num+=a[i]
print(Num)


