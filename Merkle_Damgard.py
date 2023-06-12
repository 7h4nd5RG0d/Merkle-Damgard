import math
import cmath 
import numpy as np
from cmath import exp, pi
import random

#####################################################################################################
def COMPRESS(z,m,t):  # the compression function that takes (m+t)bit input and gives a random m bit output
    A=""
    for j in range(m):
        n=random.randint(0,m+t-1)
        A=A+z[n]
    return A  #if compression function does not have collision then the hash function will also be collision resistant
#####################################################################################################

if __name__=='__main__':
    x=input("Enter the message to be hashed: ")
    #########################################################################################################

    res = ''.join(format(ord(i), '08b') for i in x)  #converting the message to binary format
    A=str(res)         
    #########################################################################################################

    m=int(input("Enter m,the length that you want the hash to be: "))
    t=int(input("Enter t,the compression function will compress by 't' bits: "))
    ########################################################################################################

    if t==1:
        y=[] 
        n=len(A)
        y.append("1")  #intially keep y[0]=1,y[1]=1
        y.append("1") 
        for j in range(n):
            if A[j]=='1':   # if you get a '1' then append '01' to the list
                y.append("0")
                y.append("1")
            else:
                y.append("0") # if you get a '0' then append '0' to the list
        pad=""  # intialise the padding..
        for j in range(m):
            pad=pad+'0'  # padding  'm' 0's    
        z1=pad+y[0]
        g=[]  # stores the final results..
        g.append(COMPRESS(z1,m,t))
        for j in range (1,len(y)):
            G=g[j-1]+y[j]
            g.append(COMPRESS(G,m,t))   
        print("Hash of the message: ",g[len(y)-1])
    #####################################################################################################
    elif t>=2 and t<=(len(A)+1):
        y=[]
        n=len(A)
        k=int(n/(t-1)) #no of blocks intially
        d=k*(t-1)-n  #length of the padding needed
        for i in range(1,k):
            y.append(A[((i-1)*(t-1)):(i*(t-1))]) 
        pad=""
        for j in range(d):
            pad=pad+'0'
        y_k=A[((k-1)*(t-1)):len(A)]+pad
        y.append(y_k)
        y_l="" # stores the binary representation of d
        while d>0:  #function to get the binary value of d to (t-1) bits 
            if d%2==1:
                y_l='1'+y_l
            else:
                y_l='0'+y_l
            d=d/2  
        while len(y_l)!=(t-1):
            y_l='0' +y_l
        y.append(y_l)
        pad1="" #initial padding
        for j in range(m+1):
            pad1=pad1+'0'
        z1=pad1+y[0]
        g=[]   #stores the final values
        g.append(COMPRESS(z1,m,t))
        for j in range(0,k):
            z=g[j]+'1'+y[j+1]
            g.append(COMPRESS(z,m,t))   
        print("Hash of the message:",g[k])
    #####################################################################################################            
    else:
        print("t has to be greater than 0 and less than the length of the meassage in binary")
    #####################################################################################################
