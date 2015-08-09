import base64
reference = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-"
catscue = raw_input("Cue> ")
#catscue = ".C3nZC3nZC3nYCNP1Chz6CNnY.bNjW.D3T6C3nZE3jZD3bZDa." #4890008104307
#catscue = ".C3nZC3nZC3nYCNP1Chz6CNnY.bNjW.ENbXD3vXDhrZCNfXEW." #9324627701228

cue = catscue.split('.')[3]
barcode = ""
for i in range(0,len(cue),4):
    part = cue[i:i+4]
    partcode = ""
    for c in part:
        f = reference.index(c)+32
        partcode += str(unichr(f))
    binary = ''.join(format(x-32,'b').zfill(6) for x in bytearray(partcode))
    for b in range(0,len(binary),8):
        byte = int(binary[b:b+8], 2)
        byte ^= 67
        barcode += str(unichr(byte))
print barcode
