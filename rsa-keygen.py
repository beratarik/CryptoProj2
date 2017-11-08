#this file creates a valid RSA public key / private key pair and stores them in files

import sys, getopt


def readInputs(commandl):
    pname = ''
    sname = ''
    numbits = 0
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

def main():
    pname, sname, numbits = readInputs(sys.argv[1:])
    
    print('public key is "', pname)
    print('secret key is "', sname)
    print('numbits is "', numbits)
