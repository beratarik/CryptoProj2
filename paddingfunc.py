#this is the encryption padding function
import os

def paddingFunc(message, length):
    #should return 00 02 Rand 00 message

<<<<<<< HEAD
    padded = b''
=======
    mlength = len(message)
    ##if mlength > (length-11):
     ##   print("not enough space for padding")
      ##  return 1
    
    padded = b''
    padlength = length-3
>>>>>>> e0813ba8eaf39c6ce8bbf316488ab2b8ede054a4

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
<<<<<<< HEAD

=======
    



main()
>>>>>>> e0813ba8eaf39c6ce8bbf316488ab2b8ede054a4
