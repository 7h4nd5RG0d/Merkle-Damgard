import math
import cmath 
import numpy as np
from cmath import exp, pi
import random

#####################################################################################################
def f1(B,C,D): #function for 1-20 rounds
    b1=int(B,2)
    c1=int(C,2)
    d1=int(D,2)
    S=(b1 & c1) | (~b1 & d1)
    return '{:032b}'.format(S)
#####################################################################################################
def f2(B,C,D): #function for 21-40 rounds
    b1=int(B,2)
    c1=int(C,2)
    d1=int(D,2)
    S=b1^c1^d1
    return '{:032b}'.format(S)
#####################################################################################################
def f3(B,C,D): #function for 41-60 rounds
    b1=int(B,2)
    c1=int(C,2)
    d1=int(D,2)
    S= (b1 & c1) | (c1 & d1) | (b1 & d1)
    return '{:032b}'.format(S)
#####################################################################################################
def f4(B,C,D): #function for 61-80 rounds
    b1=int(B,2)
    c1=int(C,2)
    d1=int(D,2)
    S=b1^c1^d1
    return '{:032b}'.format(S)
#####################################################################################################

if __name__=='__main__':
    x=input("Enter the message to be hashed: ")
    #########################################################################################################

    res = ''.join(format(ord(i), '08b') for i in x)  #converting the message to binary format
    A=str(res)    
         
    #########################################################################################################

    n=len(A)
    bin_A="" #stores the 64 bit binary of the length of input
    while n>0:
        if n%2==1:
            bin_A='1'+bin_A
        else:
            bin_A='0'+bin_A
        n=int(n/2)
    while len(bin_A)!=64:
        bin_A='0'+bin_A
    ########################################################################################################
    if len(A)%448!=0:  
        A=A+'1'
    while len(A)%448!=0:
        A=A+'0'
    message=[]
    a=int(len(A)/448) #no of 448-bit blocks , we then have 64+448=512 block size input where 64 bits come from the size
    for j in range(a):
        block=A[j*448:(j+1)*448]+bin_A
        message.append(block)
    
    for j in range(len(message)):
        m=message[j]
        words=[]
        for i in range(16):
            words.append(m[i*32:(i+1)*32])  #the block provides the first 16 words
        for i in range(16,80):   # recursive function to get all the 80 words
            W=int(words[i-3],2)^int(words[i-8],2)^int(words[i-16])^int(words[i-14])
            w='{:032b}'.format(W)
            w=w[1:32]+w[0]
            words.append(w)
        
        A_a=""
        B_b=""
        C_c=""
        D_d=""
        E_e=""
        A_i=""
        B_i=""
        C_i=""
        D_i=""
        E_i=""
        for j in range(32):  #initialising the 160-bit random key, which is divided into 5 32-bit blocks A,B,C,D,E
            n=random.randint(0,1)
            A_a=A_a+str(n)
            A_i=A_i+str(n)
            n=random.randint(0,1)
            B_b=B_b+str(n)
            B_i=B_i+str(n)
            n=random.randint(0,1)
            C_c=C_c+str(n)
            C_i=C_i+str(n)
            n=random.randint(0,1)
            D_d=D_d+str(n)
            D_i=D_i+str(n)
            n=random.randint(0,1)
            E_e=E_e+str(n)
            E_i=E_i+str(n)
        
        K_0="01011010100000100111100110011001" # constant for 1-20 rounds
        K_1="01101110110110011110101110100001" # constant for 21-40 rounds
        K_2="10001111000110111011110011011100" # constant for 41-60 rounds
        K_3="11001010011000101100000111010110" # constant for 61-80 rounds

        for j in range(20):  #recursive function for 1-20 rounds
            TEMP=int(words[j],2)^int(K_0,2)^int(E_e,2)^int(f1(B_b,C_c,D_d),2)^int((A_a[5:32]+A_a[0:4]),2)
            temp='{:032b}'.format(TEMP)
            E_e=D_d
            D_d=C_c
            C_c=B_b[30:32]+B_b[0:30]
            B_b=A_a
            A_a=temp
            A_I=int(A_a,2)^int(A_i,2)
            A_i='{:032b}'.format(A_I)
            B_I=int(B_b,2)^int(B_i,2)
            B_i='{:032b}'.format(B_I)
            C_I=int(C_c,2)^int(C_i,2)
            C_i='{:032b}'.format(C_I)
            D_I=int(D_d,2)^int(D_i,2)
            D_i='{:032b}'.format(D_I)
            E_I=int(E_e,2)^int(E_i,2)
            E_i='{:032b}'.format(E_I)

        
        for j in range(20): #recursive function for 21-40 rounds
            TEMP=int(words[j],2)^int(K_1,2)^int(E_e,2)^int(f2(B_b,C_c,D_d),2)^int((A_a[5:32]+A_a[0:4]),2)
            temp='{:032b}'.format(TEMP)
            E_e=D_d
            D_d=C_c
            C_c=B_b[30:32]+B_b[0:30]
            B_b=A_a
            A_a=temp
            A_I=int(A_a,2)^int(A_i,2)
            A_i='{:032b}'.format(A_I)
            B_I=int(B_b,2)^int(B_i,2)
            B_i='{:032b}'.format(B_I)
            C_I=int(C_c,2)^int(C_i,2)
            C_i='{:032b}'.format(C_I)
            D_I=int(D_d,2)^int(D_i,2)
            D_i='{:032b}'.format(D_I)
            E_I=int(E_e,2)^int(E_i,2)
            E_i='{:032b}'.format(E_I)

        for j in range(20): #recursive function for 41-60 rounds
            TEMP=int(words[j],2)^int(K_2,2)^int(E_e,2)^int(f3(B_b,C_c,D_d),2)^int((A_a[5:32]+A_a[0:4]),2)  
            temp='{:032b}'.format(TEMP)
            E_e=D_d
            D_d=C_c
            C_c=B_b[30:32]+B_b[0:30]
            B_b=A_a
            A_a=temp
            A_I=int(A_a,2)^int(A_i,2)
            A_i='{:032b}'.format(A_I)
            B_I=int(B_b,2)^int(B_i,2)
            B_i='{:032b}'.format(B_I)
            C_I=int(C_c,2)^int(C_i,2)
            C_i='{:032b}'.format(C_I)
            D_I=int(D_d,2)^int(D_i,2)
            D_i='{:032b}'.format(D_I)
            E_I=int(E_e,2)^int(E_i,2)
            E_i='{:032b}'.format(E_I)
        
        for j in range(20): #recursive function for 61-80 rounds
            TEMP=int(words[j],2)^int(K_3,2)^int(E_e,2)^int(f4(B_b,C_c,D_d),2)^int((A_a[5:32]+A_a[0:4]),2)
            temp='{:032b}'.format(TEMP)
            E_e=D_d
            D_d=C_c
            C_c=B_b[30:32]+B_b[0:30]
            B_b=A_a
            A_a=temp
            A_I=int(A_a,2)^int(A_i,2)
            A_i='{:032b}'.format(A_I)
            B_I=int(B_b,2)^int(B_i,2)
            B_i='{:032b}'.format(B_I)
            C_I=int(C_c,2)^int(C_i,2)
            C_i='{:032b}'.format(C_I)
            D_I=int(D_d,2)^int(D_i,2)
            D_i='{:032b}'.format(D_I)
            E_I=int(E_e,2)^int(E_i,2)
            E_i='{:032b}'.format(E_I)
        
        

        hash=A_i+B_i+C_i+D_i+E_i  #total 5*32=160 bits
        print("Hash: ",hash)             
