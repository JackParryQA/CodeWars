def sum_triangular_numbers(n):
    t=0
    if n>0:
        for i in range(0,n+1):
            t+=((i**2)+i)//2
            
        return t
    
    return 0
