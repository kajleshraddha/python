def fav(n):
    l=[0,1]
    if n<=1:
        return n
    else:
        for i in range(2,n+1):
            l.append(l[i-2]+l[i-1])
           
    return l[-1]
print(fav(int(input())))            
