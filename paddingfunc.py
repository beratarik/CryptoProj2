#this is the encryption padding function
import os
def paddingFunc(message, length):
    #should return 00 02 Rand 00 message

    mlength = len(message)
    if mlength > (length-11):
        print("not enough space for padding")
        return 1
    
    padded = b''
    padlength = length -11 -mlength -3

    while len(padded) < padlength:
        left = padlength - len(padded)
        
        newpad = os.urandom(left +20)
        newpad = newpad.replace(b'00', b'')
        padded = padded + newpad[:left]


    if len(padded) != padlength:
        printf("padded is the wrong size")
        return 1

    padded = b''.join([b'\x00\x02', padded, b'\x00', bytearray(message.encode('utf-8'))])
    print(padded)
    return padded

def main():
    message = str(9234532)
    padded = paddingFunc(message, 256)
    print(padded)




main()
