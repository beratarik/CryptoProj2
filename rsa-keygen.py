#this file creates a valid RSA public key / private key pair and stores them in files

import sys, getopt
import random
from math import gcd
def readInputs(commandl):
    pname = ''
    sname = ''
    numbits =0
    try:
        opts, args = getopt.getopt(commandl, "p:s:n:", ["pfile=", "sfile =", "numbits="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-p", "--pfile"):
            pname = arg
        elif opt in ("-s", "--sfile"):
            sname = arg
        elif opt in ("-n", "--numbits"):
            numbits = arg
    if(pname == ''):
        print("you have to include a public key file")
        exit(1)
    if(sname == ''):
        print("you have to include a secret key file")
        exit(1)
    if(numbits == 0):
        print("you have to include a keylength")
        exit(1)
    
    return pname, sname, numbits

#this is the function that implement miller rabin prime testing
def isPrime(bits, k):
    
    #k is the correctness factor
    if bits % 2 == 0:
        return 0
    
    #try to divide n-1 by 2 a bunch of times
    d =bits-1
    count = 0
    
    while True:
        quotient, remainder = divmod(d,2)
        
        if remainder ==1:
            break
        
        count += 1
        d = quotient
    
    for i in range (k):
        rand = random.randrange(2,bits)
        if compositeTest(bits, d, count,rand):
                return 0
    
    return 1

#this function tests for composites
def compositeTest(bits, d, count, rand):
    if pow(rand, d , bits)==1:
        return 0
    
    for i in range(count):
        if pow(rand, 2**i * d, bits)== bits-1:
            return 0
    
    return 1

#this is the function that gets random bits and then sends it to isPrime to see 
def makePrime(numbits):
    checkprime = 0
    k = 10
    while(checkprime == 0):
        bits = random.getrandbits(numbits)
        #trying to set last bit to 1, but im bad
       # bits = bitarray(bits)
       # print(bits)
       # bits = str(bits)+ str("1")
        #bits = int(bits)
        checkprime = isPrime(bits, k)

    print('bits is ' + str(bits))
    return bits
def main():
    pname, sname, numbits = readInputs(sys.argv[1:])

    print('public key is "', pname)
    print('secret key is "', sname)
    print('numbits is "', numbits)
    
    p = makePrime(int(numbits))
    q = makePrime(int(numbits))
    N = (p-1) * (q-1)
    e = 0
    if gcd(N,7) ==1:
        e = 7
    elif gcd(N, 11) ==1:
        e =11
    elif gcd(N, 13) ==1:
        e=13
    else:
        print("unlucky N value")
    #need to compute e*d = 1 % N
    # d = e^-1 mod N
    d = pow(e, -1)
    d = d % N
    f = (d * e) % N
    print("f is " + str(f))
    print("p is " +str(p))
    print("q is " +str(q))
    print("e is " +str(e))
    print("d is " +str(d))
    print("N is " +str(N))
main()
