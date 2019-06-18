#My version of Trivium
import random

reg_A = [''] * 93
reg_B = [''] * 84
reg_C = [''] * 111



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


stream = []
for i in range(100001152):
    t1 = reg_A[65] ^ reg_A[92]
    t2 = reg_B[68] ^ reg_B[83]
    t3 = reg_C[65] ^ reg_C[110]

    T1 = t1 ^ (reg_A[90] & reg_A[91]) ^ reg_B[76]
    T2 = t2 ^ (reg_B[81] & reg_B[82]) ^ reg_C[87]
    T3 = t3 ^ (reg_C[109] & reg_C[110]) ^ reg_A[68]
    for x in range(92,0,-1):
        reg_A[x] = reg_A[x-1]
    reg_A[0] = T1
    for x in range(83,0,-1):
        reg_B[x] = reg_B[x-1]
    reg_B[0] = T2
    for x in range(110,0,-1):
        reg_C[x] = reg_C[x-1]
    reg_C[0] = T3

    if(i > 1151):
        stream.append(t1^t2^t3)


bits = ''.join(list(map(str,stream)))
#print(bits, end = ' ')
#print(bits,end = ' After 1000 clock cycles\n')

f = open('data/triv_stream.txt','wt')
f.write(bits)
f.close()
