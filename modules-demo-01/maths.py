

def sum(*args):
    result=0
    for value in args:
        result+=value
    return result

def average(*args):
    return sum(*args)/len(args)

def min(x,y):
    return x if x<y else y

def main():
    print('in math.py')
    print('module name is ',__name__)
    print('testing')
    print('sum(1,2,3,4)',sum(1,2,3,4))
    print('average(1,2,3,4)',average(1,2,3,4))
    print('-'*20)
    print()

if __name__=='__main__':
    main()

