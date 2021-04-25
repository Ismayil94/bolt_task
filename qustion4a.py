def moduler(a,b,k):
    counter = 0
    for i in range(a,b+1):
        if i%k==0:
            counter+=1
        else:
            pass
    return counter

if __name__ == '__main__':
    try:
        a = int(input('A:\n'))
    except:
        raise ValueError('A should be integer!')    
    try:    
        b = int(input('B:\n'))
    except:
        raise ValueError('B should be integer!')
    try:    
        k = int(input('K:\n'))
    except:
        raise ValueError('K should be integer!')
    
    print(moduler(a,b,k))