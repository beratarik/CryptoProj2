#this file encrypts an integer using RSA

import sys, getopt


def readInputs(commandl):
    kname = ''
    iname = ''
    onmae = ""
    try:
        opts, args = getopt.getopt(commandl, "k:i:o:", ["kfile=", "ifile =", "ofile="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-k", "--kfile"):
            kname = arg
        elif opt in ("-i", "--ifile"):
            iname = arg
        elif opt in ("-o", "--ofile"):
            oname = arg
    if(oname == ''):
        print("you have to include an output file")
        exit(1)
    if(iname == ''):
        print("you have to include an input file")
        exit(1)
    if(kname == ''):
        print("must include fiel with RSA key in correct format")
        exit(1)
    
    return kname, iname, oname

def main():
    kname, iname, oname = readInputs(sys.argv[1:])

    print('key file is "', kname)
    print('input file is "', iname)
    print('output file is "', oname)

main()
