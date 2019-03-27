from shapes.triangle import Triangle

def is_of_type(obj,type):
    print('{} is of type {} : {}'.format(obj,type, isinstance(obj,type)))


def main():
    t1=Triangle()
    print(id(t1))
    is_of_type(t1, Triangle)
    is_of_type(t1, str)
    is_of_type('hello',Triangle)
    

if __name__=='__main__':
    main()
