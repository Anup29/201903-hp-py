def is_prime(number):
    if number<0: 
        number*=-1
        
    if number<2:
        return False
    
    test=2
    while test<number:
        if number%test==0:
            return False
        test+=1
        
    return True

def print_prime_range(max, min=2):
    if max<min:
        max,min=min,max

        
    number=min
    while number<max:
        if is_prime(number):
            print(number,end='\t')
        number+=1


print_prime_range(100,50)