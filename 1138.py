
n=int(input())

a=list(map(int, input().split()))
newone=[0]*n
for i in range(1, n+1):
    inputNum=a[i-1]#2 1 1 0 
    count=0
    
    for j in range(n):
        if count==inputNum and newone[j]==0:
            newone[j]=i
            break
        elif newone[j]==0:
            count+=1

print(*newone)
