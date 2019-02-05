import string
from random import *
l=list(string.ascii_lowercase)
l1=list(string.ascii_uppercase)
l2=list(string.digits)
l3=list(string.punctuation)
l4=list(string.ascii_letters+string.digits+string.punctuation)
n=int(input('enter length of password : '))
if(n>=6):
    str1=''.join(sample(l,1))
    str1=str1+''.join(sample(l1,1))
    str1=str1+''.join(sample(l2,1))
    str1=str1+''.join(sample(l3,1))
    s=n-4
    str1=str1+''.join(sample(l4,s))
    l5=list(str1)
    shuffle(l5)
    str3=''
    for i in l5:
        str3=str3+''.join(i)
    print('password : ',str3)
else:
    print('min length of password should be 6 ')



    
    
