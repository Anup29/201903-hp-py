import sys



if sys.version_info.major>=3:
    read_string=input
else:
    read_string=raw_input

#def read_string(prompt):
#    return input(prompt)

def read_int(prompt):
    return int(read_string(prompt))

def read_float(prompt):
    return float(read_string(prompt))

def read_bool(prompt):
    answer=read_string(prompt).lower()
    trues={'true','ok','fine','t','y','yes'}
    return answer in trues; # is answer present in seq

if __name__!='__main__':    
    print('loading module ',__name__)


