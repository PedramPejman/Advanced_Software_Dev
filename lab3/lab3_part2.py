__author__ = 'Pedram'
import os
import json
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


file_list = os.listdir()
count = 0
number_list = []
name_list = []
for file in file_list:
    if not os.path.isdir(file):
        f = open(file, 'r')
        #while (f.readline() != ""): count+=1
        name_list.append(file)
        number_list.append(get_file_checksum(file))
        count = 0
ret = [name_list, number_list]

file = open('file_info.txt','w')
file.write(json.dumps(ret))
file.close()


