def presents(a):
    l=['']*len(a)
    for i in range(len(a)):
        x=a[i]-1
        l[x]=i+1
    
    return l
