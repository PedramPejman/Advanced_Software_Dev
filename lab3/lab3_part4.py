__author__ = 'Pedram'
import sys
from Crypto.Cipher import DES

print("**input 1 key**")
x = sys.stdin.read(1)
print("**input message**")
message = input()

des = DES.new(x, DES.MODE_ECB)
dec = des.encrypt(message)
print(dec)

