
#string = input()
#def find(string, f):
#    if f in string:
#        return string.index(f)
#    return -1
#fs=['U','C','P','C']
#flag =True
#for i in range(4):
#    idx= find(string, fs[i])
#    if idx !=-1:
#        string = string[idx+1:]
#    else:
#        flag=False
#        break

#if flag:
#    print('I love UCPC')
#else:
#    print('I hate UCPC')

#    print(fs.index('P'))

flag=True
s=input()
def findout(string, fs):
    if fs in string:
        return string.index(fs)
    return -5

fs=['U',"P",'C','C']
for i in range(4):
    idx=findout(s, fs[i])
    if idx!=-5:
        s= s[idx+1:]
    else:
        flag=False
        break

if flag:
    print("yes")
else:
    print("no")