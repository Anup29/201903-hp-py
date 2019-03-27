import consoleinput as ci #import consoleutils and name object as ci
import primes as p
from maths import *

def main():
        
    run=True
    print('module name is ',__name__)
    #print(dir(p))
    while run:
        lo=ci.read_int('min?')
        hi=ci.read_int('max?')
        primes=p.prime_range(lo,hi)
        total=sum(*primes)
        avg=average(*primes)
        small=min(*primes)
        print('all primes',primes)
        print('sum',total)
        print('average',avg)
        print('lowest prime',small);

        run=ci.read_bool('continue?')

main()
