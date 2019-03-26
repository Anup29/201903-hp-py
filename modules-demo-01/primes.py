

def is_prime(number):
    if number<0: number*=-1
    if number<2: return False
    
    for test in range(2,number):
        if number%test==0:
            return False

    return True

def prime_range(min,max=None):
    if not max:
        min,max=0,min
    if min>max:
        min,max=max,min

    result=[]

    for number in range(min,max):
        if is_prime(number):
            result.append(number)

    return result


def main():
    print('testing primes')
    print('module name is ',__name__)
    resultSet={2:True, 3:True, 9:False,0:True, -9:False, -7: False }
    passed,failed=0,0

    for test,expected in resultSet.items():
        actual=is_prime(test)
        if actual!=expected:
            print('FAILED for is_prime( {}) => expected "{}" Found "{}" '.format(test,expected,actual))
            failed+=1
        else:
            passed+=1
    print('total passed={}\tfailed={}'.format(passed,failed))
    print('-'*20)        
    print()

if __name__=='__main__':
    main()