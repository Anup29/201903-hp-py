'''
Program should
1. take a min,max from user
2. find all primes in the range
3. find the lowest and highest primes
4. find the sum and average of all primes
5. ask user for more inputs
'''

import consoleinput as ci #import consoleutils and name object as ci
import primes as p

import maths




def main():
    run=True
    
    while run:
        lo=ci.read_int('min?')
        hi=ci.read_int('max?')
        primes=p.prime_range(lo,hi)
        sum=maths.sum(*primes)
        avg=maths.average(*primes)
        small=min(*primes)
        print('all primes',primes)
        print('sum',sum)
        print('average',avg)
        print('lowest prime',small);

        run=ci.read_bool('continue?')

main()
