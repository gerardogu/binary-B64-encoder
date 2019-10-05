import codecs
import binascii

byte = "1"
in_file = open("/tmp/Test/hello","rb")
out_file = open("/tmp/hello.b64","wb")
while byte != "":
    byte = in_file.read(128)
    encode = codecs.encode(binascii.b2a_base64(byte),"base64")
    #out_file.write("__INICIO__" + encode[0:(len(encode)-2)] + "__FIN__")
    out_file.write("__INICIO__" + encode[0:(len(encode)-2)] )
in_file.close()
out_file.close()
