import math

def is_prime(number):
    for i in range(2,int(math.sqrt(number))+1):
        if number%i==0:
            return False
        else:
            pass
    return True


def num_of_primes(a,b):
    counter = 0
    for i in range(a,b+1):
        if is_prime(i):
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
    
    print(num_of_primes(a,b))