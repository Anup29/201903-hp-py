'''
Program should
1. take a min,max from user
2. find all primes in the range
3. find the lowest and highest primes
4. find the sum and average of all primes
5. ask user for more inputs
'''
import maths
import consoleinput
import primes 

def main():
    run=True
    print(type(primes))
    print(primes.prime_range(1,10))

    # while run:
    #     min=read_int('min?')
    #     max=read_int('max?')
    #     primes=prime_range(min,max)
    #     sum=sum(*primes)
    #     avg=average(*primes)
    #     small=min(*primes)
    #     print('all primes',primes)
    #     print('sum',sum)
    #     print('average',avg)
    #     print('lowest prime',min);

    #     run=read_bool('continue?')

main()
