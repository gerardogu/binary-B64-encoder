import codecs
import binascii

def byteParser(byte):
    torun = True
    res = ""
    while torun:
        try:
            byte = byte[0:len(byte)-1]
            res = binascii.a2b_base64(codecs.decode(byte+"=","base64"))
            torun = False
        except:
            pass
    return res

byte = "1"
in_file = open("/tmp/hello.b64","rb")
out_file = open("/tmp/hello.devuelta","wb")
count = 0 
while byte != "":
    try:
        byte = in_file.read(244)
        #print byte
        if byte[0:10] == "__INICIO__": 
            byte = byte.replace("__INICIO__","")
            print "Entra1"
            out_file.write(binascii.a2b_base64(codecs.decode(byte+"=","base64")))
        else:
            bytes = byte.split("__INICIO__")
            for b in bytes:
                #print b
                out_file.write(binascii.a2b_base64(codecs.decode(b+"==","base64")))
    except:
        #if len(byte) != 244:
        #    byte = byte[0:len(byte)-2]
        ##byte = byte[0:len(byte)-1]
        out_file.write(byteParser(byte))
in_file.close()
out_file.close()
