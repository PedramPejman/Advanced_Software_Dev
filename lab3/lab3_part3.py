__author__ = 'Pedram'

import json
import os
from Crypto.Hash import MD5
def get_file_checksum(filename):
    h = MD5.new()
    chunk_size = 8192
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                break
            h.update(chunk)
    return h.hexdigest()


file = open('file_info.txt','r')
line = file.read()
list = eval(str((json.loads(line))))
file.close()

count =0
for i in range(0,len(list[0])):
    file = list[0][i]
    line_num = list[1][i]

    f = open(file,'r')
    #while (f.readline() != ""): count+=1
    #print (file + " " + str(line_num) + " " + str(get_file_checksum(file)))
    if (str(line_num) == str(get_file_checksum(file))):
        print (file + " has not been modified")
    else:
        print (file + " has been modified")
    count = 0







