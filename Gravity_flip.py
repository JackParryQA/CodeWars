def flip(d, a):

    if d=='R':
        a.sort()
    
    elif d=='L':
        a.sort(reverse=True)
    
    print(a)
    return a
