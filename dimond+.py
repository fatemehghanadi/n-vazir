
n=int(input("ENTER THE SIZE OF YOUR CHESS"))
succ2=set()
succ3=set()
succ =set()
current=[-2]*n
def make_beh(s):
    global n
    b1=[-2]*n
    b2=[-2]*n
    b3=[-2]*n
    b4=[-2]*n
    b5=[-2]*n
    b6=[-2]*n
    b7=[-2]*n
    str_b1=""
    str_b2=""
    str_b3=""
    str_b4=""
    str_b5=""
    str_b6=""
    str_b7=""
    if s in succ2:
        for ib in range(0,n):
            b1[n-1-int(s[ib])]=ib
            b7[int(s[ib])]=ib
            b2[int(s[ib])]=n-1-ib
            b5[ib]=n-1-int(s[ib])
            b3[n-1-ib]=n-1-int(s[ib])
            b6[n-1-ib]=int(s[ib])
            b4[n-1-int(s[ib])]=n-1-ib
        for jb in range(0,n):
            str_b1=str_b1+str(b1[jb])
            str_b2=str_b2+str(b2[jb])
            str_b3=str_b3+str(b3[jb])
            str_b4=str_b4+str(b4[jb])
            str_b5=str_b5+str(b5[jb])
            str_b6=str_b6+str(b6[jb])
            str_b7=str_b7+str(b7[jb])
        succ2.discard(str_b1)
        succ2.discard(str_b2)
        succ2.discard(str_b3)
        succ2.discard(str_b4)
        succ2.discard(str_b5)
        succ2.discard(str_b6)
        succ2.discard(str_b7)
        succ3.add(s)
def make_str(arr):
    string1=""
    for x in range(0,n):
        string1=string1+str(arr[x])
    return string1

def condition1(l,c):
    cnt=0
    for p in range(0,l):
        if c!= current[p]+l-p and c!=current[p] and c!=current[p]-(l-p):
            cnt=cnt+1
    if cnt==l:
        current[l]=c
        return True
    else:
        return False

def tabe(l):
    global n
    global current
    global succ
    if l==n:
        succ.add(make_str(current))
        #current[n-1]=-2
        return 0
    for q in range(0,n):
        if condition1(l,q):
            if n!=l:
                tabe(l+1)

tabe(0)
for yyy in succ:
    succ2.add(yyy)

for xxx in succ:
    make_beh(xxx)

print(len(succ3))
print(len(succ))
print(succ3)

print("all pattern:")
print(succ)
print("without repeated pattern:")
print(succ3-succ2)





