
#My version of Trivium
import random
import time
reg_A = [''] * 93
reg_B = [''] * 84
reg_C = [''] * 111

treg_A = [''] * 93
treg_B = [''] * 84
treg_C = [''] * 111

ca_rule=[3,1,2,4,1,3,4,2]
#<1452976485,1721342310, 2523490710,1520018790,1721342310,1452976485,1520018790,2523490710>

def parse_reg(ind,n):
    if n==93:
        if ind==0:
            return [0,0,reg_A[ind],reg_A[ind+1],reg_A[ind+2]]
        elif ind==1:
            return [0,reg_A[ind-1],reg_A[ind],reg_A[ind+1],reg_A[ind+2]]
        elif ind==92:
            return [reg_A[ind-2],reg_A[ind-1],reg_A[ind],0,0]
        elif ind==91:
            return [reg_A[ind-2],reg_A[ind-1],reg_A[ind],reg_A[ind+1],0]
        else:
            return [reg_A[ind-2],reg_A[ind-1],reg_A[ind],reg_A[ind+1],reg_A[ind+2]]
    if n==84:
        if ind==0:
            return [0,0,reg_B[ind],reg_B[ind+1],reg_B[ind+2]]
        elif ind==1:
            return [0,reg_B[ind-1],reg_B[ind],reg_B[ind+1],reg_B[ind+2]]
        elif ind==83:
            return [reg_B[ind-2],reg_B[ind-1],reg_B[ind],0,0]
        elif ind==82:
            return [reg_B[ind-2],reg_B[ind-1],reg_B[ind],reg_B[ind+1],0]
        else:
            return [reg_B[ind-2],reg_B[ind-1],reg_B[ind],reg_B[ind+1],reg_B[ind+2]]
    if n==111:
        if ind==0:
            return [0,0,reg_C[ind],reg_C[ind+1],reg_C[ind+2]]
        elif ind==1:
            return [0,reg_C[ind-1],reg_C[ind],reg_C[ind+1],reg_C[ind+2]]
        elif ind==110:
            return [reg_C[ind-2],reg_C[ind-1],reg_C[ind],0,0]
        elif ind==109:
            return [reg_C[ind-2],reg_C[ind-1],reg_C[ind],reg_C[ind+1],0]
        else:
            return [reg_C[ind-2],reg_C[ind-1],reg_C[ind],reg_C[ind+1],reg_C[ind+2]]

def ca(a,b,c,d,e,n):
    if n==1:
        return a^b^c^d^e
    elif n==2:
        return a^b^d^e
    elif n==3:
        return d&(1^e^a^b)|(1^d)&(1^e^a^c)
    elif n==4:
        return (1^b)&(a^d^e)|b&(1^a^c^e)


for i in [93, 84, 111]:
    for j in range(i):
        if i == 93:
            reg_A[j] = 0
        elif i == 84:
            reg_B[j] = 0
        elif i == 111:
            reg_C[j] = 0

reg_C[110] = reg_C[109] = reg_C[108] = 0

'''for i in range(80):
    reg_A[i] = random.getrandbits(1)
    reg_B[i] = random.getrandbits(1)
'''
str1 = '00101110110000000110010101111101000011011100110100101111011001010101110010011001'
str2 = '01001111010101010111110111010110101011110010110100001100010000010111101100100000'

#str1 is key and str2 is IV
for i in range(80):  # initializing key and IV
    reg_A[i] = int(str1[i])
    reg_B[i] = int(str2[i])

str1 = ''.join(list(map(str,reg_A[0:79])))
str2 = ''.join(list(map(str,reg_B[0:79])))

print ('Key:', end = ' ')
print (str1)
print ('\nIV: ', end = ' ')
print (str2)
print ()

start = time. time()
stream = []
for i in range(32):
    t1 = reg_A[65] ^ reg_A[92]
    t2 = reg_B[68] ^ reg_B[83]
    t3 = reg_C[65] ^ reg_C[110]

    T1 = t1 ^ (reg_A[90] & reg_A[91]) ^ reg_B[76]
    T2 = t2 ^ (reg_B[81] & reg_B[82]) ^ reg_C[87]
    T3 = t3 ^ (reg_C[109] & reg_C[110]) ^ reg_A[68]
    for x in range(92,0,-1):
        reg_A[x] = reg_A[x-1]
        a,b,c,d,e= parse_reg(x-1,93)
        treg_A[x] = ca(a,b,c,d,e,ca_rule[(x%8)-1])
    treg_A[0]=T1
    reg_A[0] = T1
    for x in range(83,0,-1):
        reg_B[x] = reg_B[x-1]
        a,b,c,d,e= parse_reg(x-1,84)
        treg_B[x] = ca(a,b,c,d,e,ca_rule[(x%8)-1])
    treg_B[0]=T2
    reg_B[0] = T2
    for x in range(110,0,-1):
        reg_C[x] = reg_C[x-1]
        a,b,c,d,e= parse_reg(x-1,111)
        treg_C[x] = ca(a,b,c,d,e,ca_rule[(x%8)-1])
    treg_C[0]= T3
    reg_C[0] = T3


    reg_A=treg_A
    reg_B=treg_B
    reg_C=treg_C

    if(i==31):
        end = time. time()
        print(end-start)
    if(i > 31):
        stream.append(t1^t2^t3)


bits = ''.join(list(map(str,stream)))

f = open('data/pent_stream_16.txt','wt')
f.write(bits)
f.close()
