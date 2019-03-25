x=int(input('number?'))
sign=''
if x==0:
    type='zero'
else:
    
    if x%2 == 0:
        type='even'
    else:
        type='odd'
        
    if x<0:
        sign='negative'
    else:
        sign='positive'
        
        
    
print('{} is {} {}'.format(x,sign,type))