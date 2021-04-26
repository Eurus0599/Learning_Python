def digit(fact):
    copy=fact
    s=0
    while copy>0:
        s+=copy%10
        copy//=10
    return s
    
def smith(x):
    copy=x
    s=0
    fact=2
    while copy>1:
        if copy%fact==0:
           s+=digit(fact)
           copy/=fact
        else:
            fact+=1
    if (s==digit(x)):
        print(x,"Smith number")
smith(22)


