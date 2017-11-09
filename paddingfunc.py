#this is the encryption padding function
import os
def paddingFunc(message, length):
    #should return 00 02 Rand 00 message

    padded = b''

    while len(padded) < length:
        left = length - len(padded)
        
        newpad = os.urandom(left +20)
        newpad = newpad.replace(b'00', b'')
        padded = padded + newpad[:left]


    if len(padded) != length:
        print("padded is the wrong size")
        return 1

    padded = b''.join([b'\x00\x02', padded, b'\x00', bytearray(message.encode('utf-8'))])
    return padded.rstrip()

if __name__ == "__main__":
    message = str(9234532)
    padded = paddingFunc(message, 256)
    print(padded)

